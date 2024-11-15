from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI(title="File Upload API")

# Include the API router
app.include_router(api_router, prefix="/api/v1")

