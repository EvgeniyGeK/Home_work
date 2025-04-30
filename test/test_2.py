def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{str(account_number)[-4:]}"


print(get_mask_account(1211789458745623))
