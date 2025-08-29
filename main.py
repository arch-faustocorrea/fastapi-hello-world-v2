from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI(
    title="FastAPI Hello World v2",
    description="A simple FastAPI hello world application with enhanced features",
    version="2.0.0",
)

class MessageResponse(BaseModel):
    message: str
    timestamp: datetime
    version: str

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime

@app.get("/")
async def read_root():
    """Root endpoint returning a welcome message"""
    return {
        "message": "Hello World from FastAPI v2!",
        "timestamp": datetime.now(),
        "version": "2.0.0"
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    """Personalized hello endpoint"""
    if not name or name.isspace():
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    return MessageResponse(
        message=f"Hello {name}! Welcome to FastAPI v2",
        timestamp=datetime.now(),
        version="2.0.0"
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now()
    )

@app.get("/info")
async def get_info():
    """Application information endpoint"""
    return {
        "name": "FastAPI Hello World v2",
        "version": "2.0.0",
        "description": "A simple FastAPI hello world application with enhanced features",
        "endpoints": [
            "/",
            "/hello/{name}",
            "/health",
            "/info",
            "/docs",
            "/redoc"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
