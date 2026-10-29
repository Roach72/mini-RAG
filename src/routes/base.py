from fastapi import FastAPI, APIRouter, Depends

from helpers.config import get_settings, Settings

baes_router = APIRouter(
    prefix="/api/v1",
    tags=['api_v1'],

)


@baes_router.get("/")
async def w(app_settings: Settings = Depends(get_settings)):

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        "app_name":app_name,
        "app_version":app_version,

    }
