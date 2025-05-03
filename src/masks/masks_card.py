def get_mask_card_number(number_list: int) -> str:
    """Функция маскировки номера банковской карты"""
    return (
        f"{str(number_list)[:4]} {str(number_list)[5:7]}** **** {str(number_list)[-4:]}"
    )


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{str(account_number)[-4:]}"
