from typing import List, ClassVar

from pydantic import BaseModel
from app.google.sheets import SheetsModel

class Level(SheetsModel):
    SHEET_NAME: ClassVar[str] = "levels"

    level: int
    need_exp: int
    soft_currency_reward: int
    hard_currency_reward: int


class GameConfigs(BaseModel):
    levels: List[Level]

    @classmethod
    async def load_from_sheets(cls):
        return cls(
            levels=await Level.load_from_sheets(),
        )
