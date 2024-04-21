import os
from gateway.core.auth import get_auth
from gateway.core.custom_logger import EventellaLogger
from fastapi import APIRouter, Depends, Request, HTTPException, Response
import httpx

logger = EventellaLogger(__name__)
router = APIRouter()

@router.get("/{type}/{path:path}")
@router.post("/{type}/{path:path}")
@router.put("/{type}/{path:path}")
@router.delete("/{type}/{path:path}")
async def gateway(
    type: str,
    path: str,
    request: Request,
    current_user = Depends(get_auth),  
):
    service_url = _get_service_url(type=type)
    url = f"{service_url}/{path}"
    logger.info(f"Request URL: {url}")
    headers = {key: value for key, value in request.headers.items()}
    try:
        async with httpx.AsyncClient() as client:
            if request.method == "GET":
                response = await client.get(url, headers=headers, params=request.query_params)
            elif request.method == "POST":
                response = await client.post(url, headers=headers, data=await request.body())
            elif request.method == "PUT":
                response = await client.put(url, headers=headers, data=await request.body())
            elif request.method == "DELETE":
                response = await client.delete(url, headers=headers)
            else:
                raise HTTPException(status_code=405, detail="Method not allowed")
        
        return Response(content=response.content, status_code=response.status_code, media_type="application/json")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

def _get_service_url(type: str):
    if type == "core":
        return os.getenv("CORE_API_URL")
    elif type == "ticketing":
        return os.getenv("TICKETING_API_URL")
    else:
        raise HTTPException(
            status_code=400,
            detail='Provided service type does not exist!'
        )
