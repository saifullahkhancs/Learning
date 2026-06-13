from fastapi import FastAPI

from api.v1.auth import router as auth_router
from database import init_db

app = FastAPI(title="NexusFlow Authentication API")


@app.on_event("startup")
async def on_startup():
    """Run database initializations on startup."""
    await init_db()


app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "NexusFlow auth service is running"}
