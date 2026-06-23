from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.dependencies import get_db, require_roles
from api.v1.auth import router as auth_router
from api.v1.users import router as users_router
from core.config import settings
from database import init_db
from models.roles import UserRole
from models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run database initializations on startup."""
    await init_db()
    yield


app = FastAPI(title="LinkeFlow Authentication API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "LinkeFlow auth service is running"}


@app.get("/db-check")
async def db_check(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_roles([UserRole.ADMIN.value])),
):
    """Authenticated endpoint to check database connectivity."""
    try:
        # Perform a simple query to check the connection
        await db.execute(select(1))
        return {"status": "ok", "message": "Database connection is healthy."}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database connection error: {e}",
        )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
