from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import config as env
from src.core import executor as exec
from src.routes import route

@asynccontextmanager
async def lifespan(app: FastAPI):

    # * Se precisar montar algo antes de iniciar o servidor, faça aqui

    yield

    exec.desligar_executor()

app = FastAPI( title=env.NAME, version=env.VERSION, description=env.DESCRIPTION, lifespan=lifespan )

app.include_router( route.router )

if __name__ == "__main__":
    
    import uvicorn

    uvicorn.run( "main:app", host=env.HOST, port=env.PORT, reload=env.RELOAD )