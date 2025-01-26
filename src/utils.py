import json
import logging
import os

log_directory = os.path.join("..", "logs")
log_file_path = os.path.join(log_directory, "utils.log")

logging.basicConfig()
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(log_file_path)
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_from_json(path_to_json: str):
    """
    Функция считывает данные из json файла и возвращает Python объект.
    Если файл не найден, пуст или не является списком - возвращается пустой список
    """
    logger.info("Getting started with the function")
    data = []
    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            logger.info("Reading the file")
            data = json.load(f)
    except Exception as ex:
        logger.error(f"An error has occurred: {ex}")
        return data
    logger.info("Successful completion of the program")
    return data


data_for_tests = read_from_json("../data/operations.json")
