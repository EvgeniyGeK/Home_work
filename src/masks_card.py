from loggers import get_logger

logger = get_logger(name=__file__)

logger.info("Начало работы функции get_mask_card_number")


def get_mask_card_number(number_list: str) -> str:
    """Функция маскировки номера банковской карты"""

    if len(number_list) != 16:
        logger.error("Не верный номер карты")
        return "Не верный номер карты"

    elif number_list == "":
        logger.error("Не верный номер карты")
        return "Не верный номер карты"
    else:
        logger.info("Функция get_mask_card_number успешно завершила свою работу")
        return f"{str(number_list)[:4]} {str(number_list)[4:6]}** **** {str(number_list)[-4:]}"


logger.info("Начало работы функции get_mask_account")


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if len(account_number) != 20:
        logger.error("Не верный номер счета")
        return "Не верный номер счета"
    elif account_number == ():
        logger.error("Не верный номер счета")
        return "Не верный номер счета"
    else:
        logger.info("Функция get_mask_account успешно завершила свою работу")
        return f"**{str(account_number)[-4:]}"
