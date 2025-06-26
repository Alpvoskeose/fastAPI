from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI/CD FastAPI работает!"}

@app.get("/db-url")
def get_db_url():
    return {"DATABASE_URL": os.getenv("DATABASE_URL", "не установлено")}
