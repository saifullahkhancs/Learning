import secrets
from datetime import datetime, timedelta
import hashlib
import bcrypt  # Use native bcrypt directly

from jose import jwt
from core.config import settings

def _get_clean_prehash(password: str) -> bytes:
    """
    Hashes any password down to a deterministic 64-character hex string,
    then encodes it to bytes for native bcrypt compatibility.
    """
    hex_string = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return hex_string.encode("utf-8")

def hash_password(password: str) -> str:
    # 1. Get clean 64-byte hex representation
    prehashed = _get_clean_prehash(password)
    # 2. Generate salt and hash natively
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(prehashed, salt)
    # 3. Decode to standard string for database storage
    return hashed.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        prehashed = _get_clean_prehash(plain_password)
        # Check password against stored hash bytes
        return bcrypt.checkpw(prehashed, hashed_password.encode("utf-8"))
    except Exception:
        return False

def generate_5_digit_code() -> str:
    return "".join(secrets.choice("0123456789") for _ in range(5))

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)