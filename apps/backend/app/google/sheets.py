import httpx
from pydantic import BaseModel

from app.config import env

from typing import List

class GetSheetResponse(BaseModel):
    range: str
    majorDimension: str
    values: List[List[str]]

GET_SHEET_API_URL = f"https://sheets.googleapis.com/v4/spreadsheets/{{sheet_id}}/values/{{sheet_name}}{{sheet_range}}?alt=json&key={{api_key}}"

async def get_sheet(sheet_name: str, sheet_range: str) -> GetSheetResponse:
    url = GET_SHEET_API_URL.format(
            sheet_id=env.google_sheet.id,
            api_key=env.google_sheet.api_key,
            sheet_name=sheet_name,
            sheet_range=sheet_range
        )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return GetSheetResponse.model_validate(response.json())

