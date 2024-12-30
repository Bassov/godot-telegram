from typing import List, ClassVar

import asyncio
from pydantic import BaseModel
from app.google.sheets import SheetsModel

class Level(SheetsModel):
    SHEET_NAME: ClassVar[str] = "levels"

    level: int
    need_exp: int
    soft_currency_reward: int
    hard_currency_reward: int

class Item(SheetsModel):
    SHEET_NAME: ClassVar[str] = "items"

    id: int
    name: str
    description: str

class GameConfigs(BaseModel):
    levels: List[Level]
    items: List[Item]

    @classmethod
    async def load_from_sheets(cls):
        levels, items = await asyncio.gather(
            Level.load_from_sheets(),
            Item.load_from_sheets(),
        )

        return cls(
            levels=levels,
            items=items,
        )
