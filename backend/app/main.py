from fastapi import FastAPI
from app.api import driver,telemetry

app = FastAPI(
    title="F1 Telemetry Dashboard API",
    version="1.0.0"
)

app.include_router(driver.router)
app.include_router(telemetry.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to F1 Telemetry Dashboard"
    }