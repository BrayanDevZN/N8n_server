from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import APIRouter
from src.config.settings import ENVIRONMENT

router = APIRouter(prefix=ENVIRONMENT["path"], tags=[ENVIRONMENT["path"]])

url = ENVIRONMENT["url"]

@router.post("/")
async def redirect_post():

    return RedirectResponse(
        url=url,
        status_code=307
    )


@router.get("/")
async def redirect_get():

    return RedirectResponse(
        url=url,
        status_code=307
    )


@router.patch("/")
async def redirect_patch():

    return RedirectResponse(
        url=url,
        status_code=307
    )


@router.put("/")
async def redirect_put():

    return RedirectResponse(
        url=url,
        status_code=307
    )

@router.delete("/")
async def redirect_delete():

    return RedirectResponse(
        url=url,
        status_code=307
    )