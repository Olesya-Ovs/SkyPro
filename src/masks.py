def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    mask_number = card_number.replace(card_number[6:12], "******")
    return f"{mask_number[:4]} {mask_number[4:8]} {mask_number[8:12]} {mask_number[12:]}"


card_number_mask = get_mask_card_number("7000792289606361")
print(card_number_mask)


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"


account_mask = get_mask_account("73654108430135874305")
print(account_mask)
