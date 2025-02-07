def filter_by_currency(transactions: list[dict], user_currency: str):
    """принимает список транзакций и поочередно выдает транзакции, где валюта операции соответствует заданной"""
    return (transaction for transaction in transactions
            if transaction["operationAmount"]["currency"]["name"] == user_currency)


def transaction_descriptions(transactions: list[dict]):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]



def card_number_generator():
    pass
