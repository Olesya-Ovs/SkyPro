import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("", "Введите номер счета из 20 цифр"),
    ("73654108430135874305525", "Введите номер счета из 20 цифр"),
    ("7365", "Введите номер счета из 20 цифр"),
    ("7365 4108 4301 3587 4305", "Введите номер счета из 20 цифр"),
    ("!@#$%", "Введите номер счета из 20 цифр"),
])
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [(73654108430135874305)])
def test_get_mask_account_wrong_type(account_number):
    """Тест на неверный тип входных данных"""
    with pytest.raises(TypeError):
        get_mask_card_number(account_number)


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("", "Введите номер карты из 16 цифр"),
    ("70007922896063611111", "Введите номер карты из 16 цифр"),
    ("11111", "Введите номер карты из 16 цифр"),
    ("?:%;№", "Введите номер карты из 16 цифр"),
    ("7000 7922 8960 6361", "Введите номер карты из 16 цифр"),
])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [(7000792289606361)])
def test_get_mask_card_number_wrong_type(card_number):
    """Тест на неверный тип входных данных"""
    with pytest.raises(TypeError):
        get_mask_card_number(card_number)
