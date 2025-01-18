import masks


def mask_account_card(account_card_number: str) -> str:
    """принимает на вход тип и номер карты или счета и возвращает строку со скрытым номером"""
    list_of_account_card_numbers = account_card_number.split(" ")
    only_number = list_of_account_card_numbers[-1]
    if list_of_account_card_numbers[0] == "Счет":
        account_card_number_mask = masks.get_mask_account(only_number)
    else:
        account_card_number_mask = masks.get_mask_card_number(only_number)
    return f"{" ".join(list_of_account_card_numbers[:-1])} {account_card_number_mask}"


def get_date(date: str) -> str:
    """меняет формат даты, убирая лишнее"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    return f"{day}.{month}.{year}"


my_account_card_number = mask_account_card("Счет 73654108430135874305")
print(my_account_card_number)

new_date = get_date("2024-03-11T02:26:18.671407")
print(new_date)
