def get_mask_card_number(number_list: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(number_list) != 16 or number_list == ():
        return 'Не верный номер карты'
    else:
            return (
        f"{str(number_list)[:4]} {str(number_list)[4:6]}** **** {str(number_list)[-4:]}"
    )


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account_number) != 20 or account_number == ():
        return 'Не верный номер счета'
    else:
        return f"**{str(account_number)[-4:]}"
