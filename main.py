from fastapi import FastAPI
from fastapi import Body, Cookie, File, Form, Header, Path, Query
import logging
import uvicorn

logger = logging.getLogger(__name__)
    
app = FastAPI()

@app.get("/")
def home():
    x = 'minha api esta no ar'
    return x

if __name__ == "__main__":
    logger.info("Iniciando o servidor...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)