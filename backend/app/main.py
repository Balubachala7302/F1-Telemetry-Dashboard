from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import driver,telemetry

app = FastAPI(
    title="F1 Telemetry Dashboard API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1.5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(driver.router)
app.include_router(telemetry.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to F1 Telemetry Dashboard"
    }