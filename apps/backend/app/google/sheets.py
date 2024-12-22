import httpx
from pydantic import BaseModel

from app.config import env

from typing import List, ClassVar

class SheetsModel(BaseModel):
    SHEET_NAME: ClassVar[str] = ""
    SHEET_RANGE: ClassVar[str] = "!A1:Z"

    @classmethod
    async def load_from_sheets(cls) -> List["SheetsModel"]:
        resp = await get_sheet(cls.SHEET_NAME, cls.SHEET_RANGE)
        return cls.from_sheet_data(resp.values)

    @classmethod
    def from_sheet_data(cls, data: List[List[str]]) -> List["SheetsModel"]:
        headers = data[0]
        fields = [f for f in cls.model_fields if not f.startswith('_')]
        
        # Validate all required fields are present in headers ordered
        for idx, field in enumerate(fields):
            if headers[idx] != field:
                raise ValidationError(f"Required field {field} not found in headers: {headers}")
        
        rows = data[1:]
        result = []
        for row in rows:
            # Create dict with values in same order as fields
            row_dict = {}
            for field in fields:
                col_idx = headers.index(field)
                row_dict[field] = row[col_idx]
            
            # Let pydantic handle type conversion
            result.append(cls(**row_dict))

        return result

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
