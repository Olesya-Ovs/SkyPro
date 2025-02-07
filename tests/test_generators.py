import pytest

from src.generators import filter_by_currency

@pytest.mark.parametrize("user_currency, expected", [
    ("USD", [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]),
    ("RUB", [
    {
        "id": 140011234,
        "state": "EXECUTED",
        "date": "2021-03-14T23:20:05.206878",
        "operationAmount": {"amount": "79115.90", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 11108645243227258000",
        "to": "Счет 22251667383060284222"
    }]),
])
def test_filter_by_currency_1(transactions, user_currency, expected: list[dict]):
    result = list((transaction for transaction in transactions
                   if transaction["operationAmount"]["currency"]["name"] == user_currency))
    assert result == expected
