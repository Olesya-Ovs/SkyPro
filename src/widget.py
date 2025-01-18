import masks

def mask_account_card(account_card_number: str) -> str:
    list_of_account_card_numbers = account_card_number.split(" ")
    only_number = list_of_account_card_numbers[-1]
    if list_of_account_card_numbers[1] == "Счет":
        account_card_number_mask = masks.get_mask_account(only_number)
    else:
        account_card_number_mask = masks.get_mask_card_number(only_number)
    return f"{" ".join(list_of_account_card_numbers[:-1])} {account_card_number_mask}"


my_account_card_number = mask_account_card("Visa Platinum 7000792289606361")
print(my_account_card_number)
