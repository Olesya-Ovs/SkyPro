from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

card_number_mask = get_mask_card_number("7000792289606361")
print(card_number_mask)

account_mask = get_mask_account("73654108430135874305")
print(account_mask)

my_account_card_number = mask_account_card("Счет 73654108430135874305")
print(my_account_card_number)

new_date = get_date("2024-03-11T02:26:18.671407")
print(new_date)
