from src.masks.masks_card import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if not account_card:
        return "Не верный номер карты"
    account_card_split = account_card.split()
    if "Счет" in account_card:
        return f"Счет {(get_mask_account(account_card_split[1]))}"
    card_number = []
    card_name = []
    for i in account_card_split:
        if i.isalpha():
            card_name.append(i)
        elif i.isdigit():
            card_number.append(i)
            # return get_mask_card_number("".join(card_number))
    new_number = get_mask_card_number("".join(card_number))
    if new_number == "Не верный номер карты":
        return new_number
    return f"{" ".join(card_name[:2])} {new_number}"


def get_date(new_data: str) -> str:
    """Функция преобразования даты"""
    date = new_data[:10]
    if len(date) == 0:
        raise ValueError("Указана не существующая дата")
    elif "-" not in new_data or ":" in date or "." in date or "/" in date:
        return "Указан не верный формат даты"
    elif date[:4] > "3000" or date[:4] == "0000":
        return "Указана не существующая дата"
    elif date[5:7] == "00" or date[8:10] == "00":
        return "Указана не существующая дата"
    elif int(date[5:7]) in (4, 6, 9, 11) and int(date[8:10]) > 30:
        return "Указана не существующая дата"
    elif date[5:7] == "02" and int(date[8:10]) > 28:
        return "Указана не существующая дата"
    elif "-" in date[:4]:
        return "Указан не верный формат даты"

    user_data = new_data[:10].split("-")[::-1]
    return f"{".".join(user_data)}"
