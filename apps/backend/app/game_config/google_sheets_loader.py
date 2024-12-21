from typing import List, ClassVar
from pydantic import BaseModel, ValidationError

from app.google import sheets

from .models import GameConfigs, LevelsConfig, Level

class GoogleSheet:
    class LevelsConfig(BaseModel):
        SHEET_NAME: ClassVar[str] = "levels"
        SHEET_RANGE: ClassVar[str] = "!A1:Z"

        __REQUIRED_LEVELS_COUNT: ClassVar[int] = 10 + 1 # 1 is header row
        __REQUIRED_HEADERS: ClassVar[List[str]] = ["level", "need_exp", "soft_currency_reward", "hard_currency_reward"]

        @classmethod
        def parse(cls, data: List[List[str]]) -> LevelsConfig:
            if len(data) < cls.__REQUIRED_LEVELS_COUNT:
                raise ValidationError(f"Not enough rows in table, min is: {cls.__REQUIRED_LEVELS_COUNT}")

            headers = data[0]
            for i, header in enumerate(cls.__REQUIRED_HEADERS):
                if headers[i] != header:
                    raise ValidationError(f"Header invalid, expected: {cls.__REQUIRED_HEADERS}, got: {headers}")

            rows = data[1:]
            levels = []
            for row in rows:
                level = int(row[0])
                levels.append(Level(
                    level=level,
                    need_exp=int(row[1]),
                    soft_currency_reward=int(row[2]),
                    hard_currency_reward=int(row[3])
                ))

            return levels

class Loader:
    async def load(self) -> GameConfigs:
        return GameConfigs(
            levels=await self.__load_levels(),
        )

    async def __load_levels(self) -> LevelsConfig:
        resp = await sheets.get_sheet(
            GoogleSheet.LevelsConfig.SHEET_NAME, GoogleSheet.LevelsConfig.SHEET_RANGE
        )
        return GoogleSheet.LevelsConfig.parse(resp.values)

