def filter_by_state(operations: list[dict], user_state: str = "EXECUTED") -> list[dict]:
    """принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    отфильтрованный по ключу state"""
    sorted_operations = []
    for element in operations:
        if element["state"] == user_state:
            sorted_operations.append(element)
    return sorted_operations


def sort_by_date(operations: list[dict], user_reverse: bool = True) -> list[dict]:
    """принимает список словарей, возвращает новый список, отсортированный по дате"""
    sorted_by_date_list = sorted(operations, key=lambda dictionary: (dictionary['date'], dictionary['id']),
                                 reverse=user_reverse)
    return sorted_by_date_list
