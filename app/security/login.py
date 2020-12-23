from typing import Optional

from app.db import User, get_user_by_username
from app.extensions import manager


@manager.user_loader
def load_user(username: str) -> User:
    return get_user_by_username(username)
