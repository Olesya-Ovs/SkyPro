def filter_by_currency(transactions: list[dict], user_currency: str):
    """принимает список транзакций и поочередно выдает транзакции, где валюта операции соответствует заданной"""
    # for transaction in transactions:
    #     if transaction["operationAmount"]["currency"]["name"] == user_currency:
    #         yield transaction
    return (transaction for transaction in transactions
            if transaction["operationAmount"]["currency"]["name"] == user_currency)


def transaction_descriptions():
    pass


def card_number_generator():
    pass
