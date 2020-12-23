import os
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class FakeDB(BaseModel):
    users: list[User] = []


DB = FakeDB(users=[User(username=os.getenv('ADMIN_USERNAME', 'username'),
                        password=os.getenv('ADMIN_PASSWORD', 'password'))])


def get_user_by_username(username: str) -> Optional[User]:
    for user in DB.users:
        if user.username == username:
            return user
