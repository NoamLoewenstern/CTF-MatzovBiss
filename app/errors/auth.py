from app.extensions import app, manager
from fastapi.responses import RedirectResponse


class NotAuthenticatedException(Exception):
    pass


def exc_handler(request, exc):
    return RedirectResponse(url='/login')


manager.not_authenticated_exception = NotAuthenticatedException

app.add_exception_handler(NotAuthenticatedException, exc_handler)
