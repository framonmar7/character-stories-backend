from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Character Stories API")
app.include_router(router)
