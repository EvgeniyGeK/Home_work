import pytest


@pytest.fixture
def test_number():
    """Для функции masks_card"""
    return "7000792289606361"


@pytest.fixture
def test_account():
    """Для функции masks_account"""
    return "73654108430135874305"


@pytest.fixture
def test_account_card():
    """Для функции account_card"""
    return "Счет 64686473678894779589"


@pytest.fixture
def test_date():
    """Для функции date"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def test_filter():
    """Для функции filter"""
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]


@pytest.fixture
def test_filter_2():
    """Для функции filter"""
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "NOT FULFILLED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]


@pytest.fixture
def test_sorty():
    """Для функции sorty"""
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

@pytest.fixture
def test_sorty_2():
    """Для функции sorty"""
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]

@pytest.fixture
def test_sorty_3():
    """Для функции sorty"""
    return [{"id": 41428829, "state": "EXECUTED"},
            {"id": 939719570, "state": "EXECUTED"},
                           ]
@pytest.fixture
def test_filter_currency():
    """Тест функции генератора которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    return (
    [
       {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

@pytest.fixture
def test_transaction_descriptions_fix():
    """Тест функции генератора которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    return (
    [
       {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }])
