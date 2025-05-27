from fastapi import APIRouter

from app.services.healthService import returnHealth

router = APIRouter()

@router.get('/health-check', tags=['health'])
async def getHealth(status: str = 'good'):
    return {'health': await returnHealth(True if status=='good' else False)}