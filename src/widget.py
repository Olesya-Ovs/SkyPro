from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """принимает на вход тип и номер карты или счета и возвращает строку со скрытым номером"""
    list_of_account_card_numbers = account_card_number.split(" ")
    only_number = list_of_account_card_numbers[-1]
    if list_of_account_card_numbers[0] == "Счет":
        account_card_number_mask = get_mask_account(only_number)
    else:
        account_card_number_mask = get_mask_card_number(only_number)
    return f"{" ".join(list_of_account_card_numbers[:-1])} {account_card_number_mask}"


def get_date(date: str) -> str:
    """меняет формат даты, убирая лишнее"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    return f"{day}.{month}.{year}"
