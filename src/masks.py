def get_mask_card_number(card_number: str,) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if not isinstance(card_number, str):
        raise TypeError("Ошибка типа данных")
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number.replace(card_number[6:12], "******")
        return f"{mask_number[:4]} {mask_number[4:8]} {mask_number[8:12]} {mask_number[12:]}"
    else:
        return "Введите номер карты из 16 цифр"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if not isinstance(account_number, str):
        raise TypeError("Ошибка типа данных")
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Введите номер счета из 20 цифр"
