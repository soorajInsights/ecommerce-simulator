from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="E-commerce Simulator",
    version="0.1.0"
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "project": "E-commerce Simulator",
        "status": "running"
    }