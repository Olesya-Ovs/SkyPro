import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('state, expected', [
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ]),
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]),
    ('STOPED', []),
])
def test_filter_by_state(all_operations: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(all_operations, state) == expected


@pytest.mark.parametrize('user_reverse, expected', [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ]),
])
def test_sort_by_date_1(all_operations: list[dict], user_reverse: bool, expected: list[dict]) -> None:
    assert sort_by_date(all_operations, user_reverse) == expected


@pytest.mark.parametrize('user_reverse, expected', [
    (True, [
        {'id': 99928829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]),
    (False, [
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 99928829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ]),
])
def test_sort_by_date_2(same_date_operations: list[dict], user_reverse: bool, expected: list[dict]) -> None:
    assert sort_by_date(same_date_operations, user_reverse) == expected
