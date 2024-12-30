import pytest
from pytest_mock import MockerFixture
from typing import Optional, List

from .sheets import SheetsModel, GetSheetResponse


class SheetExample(SheetsModel):
    SHEET_NAME = "sheet_example"

    id: int
    name: str
    value: Optional[str] = None
    float_value: float # in google sheets it has format "1,0"


sheet_example_valid_tests = [
    # header only
    (
        [["id", "name", "value", "float_value"]], # values from google sheets request
        []                         # expected parsed result
    ),
    # all values
    (
        [["id", "name", "value", "float_value"], ["1", "test1", "value1", "1,0"]],
        [SheetExample(id=1, name="test1", value="value1", float_value=1.0)]
    ),
    # missing value
    (
        [["id", "name", "value", "float_value"], ["1", "test1", "", "1,0"]],
        [SheetExample(id=1, name="test1", float_value=1.0)]
    )
]

def get_sheets_response(values):
    return GetSheetResponse(
        range="sheet_example!A1:Z",
        majorDimension="ROWS",
        values=values
    )

@pytest.mark.asyncio
@pytest.mark.parametrize("google_sheets_values,expected", sheet_example_valid_tests)
async def test_load_from_sheets(
    mocker: MockerFixture,
    google_sheets_values: List[List[str]],
    expected: List[SheetExample]
):
    mocker.patch('app.google.sheets.get_sheet', return_value=get_sheets_response(google_sheets_values))
    result = await SheetExample.load_from_sheets()
    print(result)
    assert result == expected

sheet_example_invalid_tests = [
    # empty values
    ([]),
    # wrong header
    ([["wrong_header"]]),
    # missing header
    ([["id", "name"]]),
    # missing value
    ([["id", "name", "value", "float_value"], ["1", "", "", "1,0"]]),
    # wrong value type
    ([["id", "name", "value", "float_value"], ["test", "test", "test", "test"]]),
]

@pytest.mark.asyncio
@pytest.mark.parametrize("google_sheets_values", sheet_example_invalid_tests)
async def test_load_from_sheets_invalid(mocker: MockerFixture, google_sheets_values: List[List[str]]):
    mocker.patch('app.google.sheets.get_sheet', return_value=get_sheets_response(google_sheets_values))
    with pytest.raises(ValueError):
        await SheetExample.load_from_sheets()
