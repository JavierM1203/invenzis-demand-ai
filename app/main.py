from fastapi import FastAPI
from app.api import discovery
from app.api import research

app = FastAPI(
    title="DemandAI",
    version="0.1.0"
)

app.include_router(discovery.router)
app.include_router(research.router)

@app.get("/")
def root():
    return {"message": "DemandAI Backend"}