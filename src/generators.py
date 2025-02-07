


def filter_by_currency(transactions: list[dict], user_currency: str) -> dict:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == user_currency:
            yield transaction



def transaction_descriptions():
    pass


def card_number_generator():
    pass
