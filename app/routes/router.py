"""
API route definitions for health check endpoints.

This module contains all the FastAPI route handlers for the health check functionality.
"""

from fastapi import APIRouter

from app.services.healthService import returnHealth

router = APIRouter()


@router.get('/health-check', tags=['health'])
async def getHealth(status: str = 'good'):
    """
    Get the health status of the application.
    
    Args:
        status (str): The desired health status. Use 'good' for healthy status,
                     any other value for degraded status. Defaults to 'good'.
    
    Returns:
        dict: A dictionary containing the health status message.
    """
    return {'health': await returnHealth(True if status == 'good' else False)}