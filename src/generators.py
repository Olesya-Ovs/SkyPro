def filter_by_currency(transactions: list[dict], user_currency: str):
    """принимает список транзакций и поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions
            if transaction["operationAmount"]["currency"]["name"] == user_currency)


def transaction_descriptions(transactions: list[dict]):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]



def card_number_generator(start: int, stop: int) -> str:
    """выдает номера банковских карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for num in range(start, stop + 1):
        str_num = f"{num:016}"
        yield f"{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:16]}"
