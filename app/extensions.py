import os

from fastapi import FastAPI
from fastapi_login import LoginManager

app = FastAPI()
manager = LoginManager(os.environ['LOGIN_MANAGER_PASSWORD'], tokenUrl='/auth')
