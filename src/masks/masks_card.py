import logging
from loggers import get_logger


logger = get_logger()

logger.info(f"Начало работы функции get_mask_card_number")
def get_mask_card_number(number_list: str) -> str:
    """Функция маскировки номера банковской карты"""

    if len(number_list) != 16:
        logger.error(f'Не верный номер карты')
        return "Не верный номер карты"

    elif number_list == "":
        logger.error(f'Не верный номер карты')
        return "Не верный номер карты"
    else:
        logger.info(f"Функция get_mask_card_number успешно завершила свою работу")
        return f"{str(number_list)[:4]} {str(number_list)[4:6]}** **** {str(number_list)[-4:]}"


print(get_mask_card_number("1234567891023456"))


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if len(account_number) != 20:

        return "Не верный номер счета"
    elif account_number == ():

        return "Не верный номер счета"
    else:

        return f"**{str(account_number)[-4:]}"
