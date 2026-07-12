from fastapi import FastAPI

app = FastAPI(
    title="F1 Telemetry Dashboard API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to F1 Telemetry Dashboard"
    }