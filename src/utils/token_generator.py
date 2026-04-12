import os
import uuid
from datetime import datetime, timedelta, timezone

import jwt

SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
ALGORITHM = "HS256"


def create_jwt(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def generate_random_token():
    return uuid.uuid4().hex
