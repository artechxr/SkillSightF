import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router

app = FastAPI(title="SkillSight AI Labour Market Intelligence API", version="2.1.0")

# Set CORS_ORIGINS to comma-separated frontend origins in deployment.
# Local development defaults to the Next.js development and production origins.
_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
_allowed_origins = [origin.strip() for origin in _origins.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def home():
    return {"status": "ok", "message": "SkillSight API is running", "data_mode": "SIMULATED"}

@app.get("/health")
def health():
    return {"status": "ok"}
