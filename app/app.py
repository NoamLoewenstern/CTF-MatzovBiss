from fastapi import Depends, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_login.exceptions import InvalidCredentialsException

from app.config import FRONTEND_DIRECTORY

from .extensions import app, manager
from .security.login import load_user

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIRECTORY / "static")), name="static")
templates = Jinja2Templates(directory=str(FRONTEND_DIRECTORY))


@app.get('/', response_class=HTMLResponse)
@app.get('/auth', response_class=HTMLResponse)
@app.get('/login', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/favicon.ico')
def favicon():
    return FileResponse(FRONTEND_DIRECTORY / 'favicon.ico')


@app.post('/auth')
@app.post('/login')
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    user = load_user(username)
    if not user or password != user.password:
        return templates.TemplateResponse('index.html', {'request': request, 'invalid_creds': True})
        # raise InvalidCredentialsException

    access_token = manager.create_access_token(data=dict(sub=username))
    # return {'access_token': access_token, 'token_type': 'bearer'}

    return templates.TemplateResponse('index.html', {'request': request, 'logged_in': True})
