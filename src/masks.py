def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    mask_number = card_number.replace(card_number[6:12], "******")
    return f"{mask_number[:4]} {mask_number[4:8]} {mask_number[8:12]} {mask_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[-4:]}"
