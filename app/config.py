from pathlib import Path

SERVER_DIRECTORY = Path(__file__).parent.parent.resolve().absolute()
FRONTEND_DIRECTORY = SERVER_DIRECTORY / 'frontend'
print(f'{SERVER_DIRECTORY=}')
print(f'{FRONTEND_DIRECTORY=}')
