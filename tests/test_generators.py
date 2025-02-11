import pytest

from src.generators import card_number_generator, transaction_descriptions


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
def test_filter_by_currency_1(transactions: list[dict], user_currency: str, expected: list[dict]) -> None:
    result = list((transaction for transaction in transactions
                   if transaction["operationAmount"]["currency"]["name"] == user_currency))
    assert result == expected


def test_transaction_descriptions(transactions: list[dict]) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"]),
    (4055, 4057, ["0000 0000 0000 4055",
                  "0000 0000 0000 4056",
                  "0000 0000 0000 4057"]),
    (5, 1, [])
])
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
