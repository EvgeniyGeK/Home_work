from src.masks.masks_card import get_mask_card_number
from src.masks.masks_card import get_mask_account


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


print(mask_account_card("Счет 64686473678894779589"))

# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305)
