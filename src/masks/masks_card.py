import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('..Home_work/logs/masks.log')
file_formater = logging.Formatter('%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s : %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
def get_mask_card_number(number_list: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info(f'Получен номер банковской карты: {number_list}')
    if len(number_list) != 16:
        logger.error(f'Произошла ошибка: Введен не верный номер карты')
        return "Не верный номер карты"
    elif number_list == "":
        logger.error(f'Произошла ошибка: Отсутствует номер карты')
        return "Не верный номер карты"
    else:
        logger.info(f'Номер карты скрыт: {str(number_list)[:4]} {str(number_list)[4:6]}** **** {str(number_list)[-4:]}')
        return f"{str(number_list)[:4]} {str(number_list)[4:6]}** **** {str(number_list)[-4:]}"

get_mask_card_number('1234567891023456')

def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info(f'Получен номер счета: {account_number}')
    if len(account_number) != 20:
        logger.error(f'Произошла ошибка: Введен не верный номер счета')
        return "Не верный номер счета"
    elif account_number == ():
        logger.error(f'Произошла ошибка: Отсутствует номер счета')
        return "Не верный номер счета"
    else:
        logger.info(f'Номер счета скрыт: "**{str(account_number)[-4:]}"')
        return f"**{str(account_number)[-4:]}"
