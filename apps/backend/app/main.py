from fastapi import FastAPI

from app.game_config.api import game_configs_router

app = FastAPI()
app.include_router(game_configs_router)
