from fastapi import FastAPI
from src.config import env_config as env

app = FastAPI( title=env.NAME, version=env.VERSION, description=env.DESCRIPTION )

if __name__ == "__main__":
    
    import uvicorn

    uvicorn.run( app, host=env.HOST, port=env.PORT, reload=env.RELOAD )