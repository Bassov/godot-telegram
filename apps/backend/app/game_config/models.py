from typing import List

from pydantic import BaseModel

class Level(BaseModel):
    level: int
    need_exp: int
    soft_currency_reward: int
    hard_currency_reward: int

LevelsConfig = List[Level]

class GameConfigs(BaseModel):
    levels: LevelsConfig
