from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import async_session
from core.security import (
    create_access_token,
    create_refresh_token,
    generate_5_digit_code,
    hash_password,
    verify_password,
)
from models.user import User
from schemas.auth import Token, UserLogin, UserRegister, VerifyEmail

router = APIRouter(prefix="/api/v1/auth")


async def get_db() -> AsyncSession:
    """Dependency to get an async database session."""
    async with async_session() as session:
        yield session


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_in: UserRegister, db: AsyncSession = Depends(get_db)):
    verification_code = generate_5_digit_code()
    user = User(
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
        is_verified=False,
        verification_code=verification_code,
    )

    db.add(user)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="User already exists")

    # Mock email send for now
    # TODO: send verification code via email instead of logging
    import logging
    logging.getLogger(__name__).info("Verification code generated for %s", user.email)
    return {"message": "Verification code sent to email"}


@router.post("/verify-email")
async def verify_email(data: VerifyEmail, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalars().first()

    if user is None or user.verification_code != data.code:
        raise HTTPException(status_code=400, detail="Invalid code or email")

    user.is_verified = True
    user.verification_code = None
    await db.commit()
    return {"message": "Account verified successfully"}


@router.post("/login", response_model=Token)
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == credentials.email))
    user = result.scalars().first()

    if user is None or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Please verify your email first")

    access_token = create_access_token({"sub": user.email})
    refresh_token = create_refresh_token({"sub": user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
