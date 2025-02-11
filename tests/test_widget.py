import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("account_card_number, expected", [
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("", "Введите номер карты или счета"),
])
def test_mask_account_card(account_card_number: str, expected: str) -> None:
    assert mask_account_card(account_card_number) == expected


@pytest.mark.parametrize("date, cleaned_date", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("", "Введите дату"),
])
def test_get_date(date: str, cleaned_date: str) -> None:
    assert get_date(date) == cleaned_date
