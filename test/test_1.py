def get_mask_card_number(number_list: int) -> str:
    """Функциz маскировки номера банковской карты"""
    return f"{str(number_list)[:4]} {str(number_list)[5:7]}** **** {str(number_list)[-4:]}"


print(get_mask_card_number(1211789458745623))
