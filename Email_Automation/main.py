import os
import smtplib
from contextlib import asynccontextmanager
from email.message import EmailMessage
from email.utils import formataddr
# pyrefly: ignore [missing-import]
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from enum import Enum
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
import uvicorn

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.future import select

# Load environment variables
load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "").replace(" ", "")
SMTP_SENDER_NAME = os.getenv("SMTP_SENDER_NAME", "Saifullah Khan")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/email_automation")

# SQLAlchemy setup
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class JobTemplate(Base):
    __tablename__ = "job_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    context = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    cv_bytes = Column(LargeBinary, nullable=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(title="Local Email Automation System", lifespan=lifespan)

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobType(str, Enum):
    python_dev = "Python Developer"
    fullstack_dev = "Full Stack Developer"


@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    """
    Serve a simple HTML UI to allow multiline text areas.
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Email Automation UI</title>
        <style>
            body { font-family: sans-serif; margin: 40px; max-width: 800px; background: #f4f7f6; color: #333; }
            .card { background: white; border: 1px solid #ddd; padding: 25px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            label { display: block; margin-top: 15px; font-weight: bold; color: #555; }
            input, select, textarea { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-family: sans-serif; }
            textarea { height: 200px; resize: vertical; white-space: pre-wrap; }
            button { margin-top: 20px; padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; }
            button:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h1>Email Automation System</h1>
        
        <div class="card">
            <h2>1. Upload / Update Job Template</h2>
            <form action="/upload" method="POST" enctype="multipart/form-data">
                <label>Job Type</label>
                <select name="type">
                    <option value="Python Developer">Python Developer</option>
                    <option value="Full Stack Developer">Full Stack Developer</option>
                </select>
                
                <label>Email Subject (Title)</label>
                <input type="text" name="title" required placeholder="Application for Python Developer">
                
                <label>Email Body (Context)</label>
                <textarea name="context" required placeholder="Dear Hiring Manager,\n\nI am writing to apply for the Python Developer position..."></textarea>
                
                <label>CV (PDF only)</label>
                <input type="file" name="cv_pdf" accept="application/pdf" required>
                
                <button type="submit">Upload Template</button>
            </form>
        </div>

        <div class="card">
            <h2>2. Send Email</h2>
            <form action="/send" method="POST">
                <label>Recipient Email</label>
                <input type="email" name="recipient_email" required placeholder="hr@company.com">
                
                <label>Job Type</label>
                <select name="type">
                    <option value="Python Developer">Python Developer</option>
                    <option value="Full Stack Developer">Full Stack Developer</option>
                </select>
                
                <button type="submit">Send Email</button>
            </form>
        </div>
    </body>
    </html>
    """
    return html

@app.get("/api/types")
async def list_types():
    """
    Endpoint to list all available types currently stored in DB.
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(JobTemplate.type))
        types = result.scalars().all()
    return {"available_types": types}

@app.post("/upload")
async def upload_job(
    type: JobType = Form(...),
    title: str = Form(...),
    context: str = Form(...),
    cv_pdf: UploadFile = File(...)
):
    """
    Upload endpoint to store job type details and CV into PostgreSQL.
    """
    if cv_pdf.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be a PDF"
        )
    
    cv_bytes = await cv_pdf.read()
    
    async with AsyncSessionLocal() as session:
        # Check if type exists
        result = await session.execute(select(JobTemplate).where(JobTemplate.type == type.value))
        job = result.scalars().first()
        
        if job:
            job.title = title
            job.context = context
            job.cv_bytes = cv_bytes
            job.filename = cv_pdf.filename
        else:
            job = JobTemplate(
                type=type.value,
                title=title,
                context=context,
                cv_bytes=cv_bytes,
                filename=cv_pdf.filename
            )
            session.add(job)
            
        await session.commit()
    
    return {
        "message": "Upload successful",
        "type": type,
        "preview": {
            "title": title,
            "context": context[:50] + "..." if len(context) > 50 else context,
            "filename": cv_pdf.filename,
            "file_size_bytes": len(cv_bytes)
        }
    }

@app.post("/send")
async def send_email(
    recipient_email: EmailStr = Form(...),
    type: JobType = Form(...)
):
    """
    Send endpoint to shoot email to recipient using stored data from DB for the given type.
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(JobTemplate).where(JobTemplate.type == type.value))
        job_data = result.scalars().first()
        
    if not job_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job type '{type.value}' not found."
        )
    
    msg = EmailMessage()
    msg["Subject"] = job_data.title
    msg["From"] = formataddr((SMTP_SENDER_NAME, SMTP_USER))
    msg["To"] = recipient_email
    
    # Set plain text content first
    msg.set_content(job_data.context)
    
    # Add HTML alternative to preserve formatting/newlines safely for all email clients
    html_content = job_data.context.replace("\r\n", "\n").replace("\n", "<br>")
    html_body = f"""\
<html>
  <body style="font-family: sans-serif; font-size: 14px; line-height: 1.5;">
    {html_content}
  </body>
</html>
"""
    msg.add_alternative(html_body, subtype='html')
    
    # Attach the PDF
    msg.add_attachment(
        job_data.cv_bytes,
        maintype="application",
        subtype="pdf",
        filename=job_data.filename
    )
    
    try:
        if SMTP_PORT == 465:
            # Connect via SSL
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
        else:
            # Connect via TLS
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.send_message(msg)
                
        return {"message": "Email sent successfully", "recipient": recipient_email}
    except smtplib.SMTPAuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"SMTP Authentication error: Check your email and app password. Details: {str(e)}"
        )
    except smtplib.SMTPException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"SMTP error occurred: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
