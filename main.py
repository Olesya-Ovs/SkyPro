from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number_mask = get_mask_card_number("7000792289606361")
print(card_number_mask)

account_mask = get_mask_account("73654108430135874305")
print(account_mask)

my_account_card_number = mask_account_card("Счет 73654108430135874305")
print(my_account_card_number)

my_account_card_number = mask_account_card("Visa Platinum 7000792289606361")
print(my_account_card_number)

new_date = get_date("2024-03-11T02:26:18.671407")
print(new_date)

my_sorted_list_by_state = filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED')
print(my_sorted_list_by_state)

my_sorted_list_by_state = filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'STOPED')
print(my_sorted_list_by_state)

my_sorted_list_by_date = sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 139719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],)
print(my_sorted_list_by_date)
