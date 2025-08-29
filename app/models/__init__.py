from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageResponse(BaseModel):
    """Standard message response model"""
    message: str
    timestamp: datetime
    version: str

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    timestamp: datetime

class GreetingRequest(BaseModel):
    """Request model for custom greetings"""
    name: str
    message: Optional[str] = None

class ErrorResponse(BaseModel):
    """Standard error response model"""
    error: str
    detail: Optional[str] = None
    timestamp: datetime
    status_code: int
