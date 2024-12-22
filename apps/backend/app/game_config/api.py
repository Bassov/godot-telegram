from fastapi import APIRouter

from .models import GameConfigs

game_configs_router = APIRouter(prefix="/game_configs", tags=["game_configs"])

@game_configs_router.get("/")
async def get_configs() -> GameConfigs:
    return await GameConfigs.load_from_sheets()
