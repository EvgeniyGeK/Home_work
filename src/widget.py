from src.masks.masks_card import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if "Счет" in account_card:
        return f"Счет {(get_mask_account(account_card))}"
    card_number = []
    card_name = []
    for i in account_card:
        if i.isalpha():
            card_name.append(i)
        elif i.isdigit():
            card_number.append(i)
    return f"{"".join(card_name)} {get_mask_card_number("".join(card_number))}"


def get_date(new_data: str) -> str:
    """Функция преобразования даты"""
    user_data = new_data[:10].split("-")[::-1]
    return f"{".".join(user_data)}"
