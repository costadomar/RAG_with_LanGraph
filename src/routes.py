from fastapi import FastAPI, HTTPException, Request, status
from chainlit.utils import mount_chainlit
from dotenv import load_dotenv

load_dotenv("../.env")

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}

mount_chainlit(app=app, target="service/app.py", path="/assistente")