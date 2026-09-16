from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import APIRouter, Request, Response
from src.config.settings import ENVIRONMENT
import requests
router = APIRouter(prefix="/auth", tags=["auth"])

url = "http://n8n:5678"


@router.api_route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
async def redirect_get():

    return Response(
        status_code=200
    )





    