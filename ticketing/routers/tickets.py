import os
from ticketing.core.auth import get_auth
from ticketing.core.custom_logger import EventellaLogger
from fastapi import APIRouter, Depends, Request, HTTPException, Response
import httpx

logger = EventellaLogger(__name__)
router = APIRouter()

@router.get("/preview")
async def preview_ticket(
    current_user = Depends(get_auth),  
):
    return True

@router.get("/buy")
async def buy_ticket(
    current_user = Depends(get_auth),  
):
    return True