def filter_by_state(list_of_dict: list, user_state: str = "EXECUTED") -> list:
    """принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    отфильтрованный по ключу state"""
    sorted_list_of_dict = []
    for element in list_of_dict:
        if element["state"] == user_state:
            sorted_list_of_dict.append(element)
    return sorted_list_of_dict


def sort_by_date(list_of_dict: list, user_reverse: bool = True) -> list:
    """принимает список словарей, возвращает новый список, отсортированный по дате"""
    sorted_by_date_list = sorted(list_of_dict, key=lambda dictionary: dictionary['date'], reverse=user_reverse)
    return sorted_by_date_list
