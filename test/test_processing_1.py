import pytest



from src.processing import filter_by_state


def test_filter_by_state(test_filter):
    assert filter_by_state(test_filter) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]




def test_filter_by_state_1(test_filter_2):
    assert filter_by_state(test_filter_2) ==  [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ]
