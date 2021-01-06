import os

import uvicorn

from app import app

if __name__ == "__main__":
    uvicorn.run('app:app',
                host=os.getenv('HOST', '0.0.0.0'),
                port=int(os.getenv('PORT', 80)),
                reload=True,
                debug=True,
                )
