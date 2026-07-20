from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies import get_db
from api.v1 import templates
from core.email import send_job_application_email

router = APIRouter()


@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}


@router.get("/job-types")
async def get_job_types():
    """List available job type options."""
    return await templates.list_job_types()


@router.get("/templates")
async def get_templates():
    """List all templates (metadata only)."""
    return await templates.list_templates()


@router.get("/templates/{job_type}")
async def get_template_details(job_type: str):
    """Get full template details for a job type."""
    return await templates.get_template(job_type)


@router.get("/templates/{job_type}/cv")
async def download_template_cv(job_type: str):
    """Download/preview the CV PDF for a job type."""
    return await templates.download_cv(job_type)


@router.post("/templates", status_code=status.HTTP_201_CREATED)
async def create_new_template(
    type: templates.JobType = Form(...),
    title: str = Form(...),
    context: str = Form(...),
    cv_pdf: UploadFile = File(...),
):
    """Create a new job application template."""
    return await templates.create_template(
        type=type, title=title, context=context, cv_pdf=cv_pdf
    )


@router.patch("/templates/{job_type}")
async def update_template(
    job_type: str,
    title: Optional[str] = Form(None),
    context: Optional[str] = Form(None),
    cv_pdf: Optional[UploadFile] = File(None),
):
    """Update the title, context, and/or CV for a template."""
    return await templates.patch_template(
        job_type=job_type, title=title, context=context, cv_pdf=cv_pdf
    )


@router.post("/send")
async def send_application_email(
    request: templates.SendEmailRequest, db: AsyncSession = Depends(get_db)
):
    """Send a job application email using a stored template."""
    job = await templates.get_template_by_type(db, request.type)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job type '{request.type}' not found.",
        )

    await send_job_application_email(
        recipient_email=request.recipient_email,
        subject=job.title,
        context=job.context,
        cv_bytes=job.cv_bytes,
        cv_filename=job.filename,
    )
    return {"message": "Email sent successfully."}