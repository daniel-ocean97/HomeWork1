import logging
import os

log_directory = os.path.join("..", "logs")
log_file_path = os.path.join(log_directory, "masks.log")

logging.basicConfig()
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_file_path)
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску номера карты.
    Передаваемое значение должно быть приведено к строковому типу в момент вызова"""
    logger.info('Getting started with the function "get_mask_card_number"')
    if not card_number.isdigit() or len(card_number) != 16:
        logger.info("Incorrect card number entered")
        return "Введён некорректный номер карты"
    logger.info("The card number is being formatted")
    for i in range(4, len(card_number), 5):
        card_number = card_number[:i] + " " + card_number[i:]
    card_number_list = card_number.split()
    card_number_list[1] = card_number_list[1][:2] + "**"
    card_number_list[2] = "****"
    logger.info("Successful completion of the program")
    return " ".join(card_number_list)


def get_mask_account(account: str) -> str:
    """Функция, которая создает маску номер счета
    Передаваемое значение должно быть приведено к строковому типу в момент вызова"""
    logger.info('Getting started with the function "get_mask_account"')
    if not account.isdigit() or len(account) != 20:
        logger.info("Incorrect account number entered")
        return "Введён некорректный номер счёта"
    logger.info("Successful completion of the program")
    return "**" + account[-4:]
