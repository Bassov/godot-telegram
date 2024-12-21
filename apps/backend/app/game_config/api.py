from fastapi import APIRouter

from .google_sheets_loader import Loader
from .models import GameConfigs

game_configs_router = APIRouter(prefix="/game_configs", tags=["game_configs"])

@game_configs_router.get("/")
async def get_configs() -> GameConfigs:
    config = await Loader().load()
    return config