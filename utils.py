import json
from datetime import datetime

def get_operations_json(filename) -> list:
    """
    Функция возвращает преобразованный в python формат список операций
    :param filename: Файл json-формата
    :return: список данных, полученных из filename
    """
    with open(filename, encoding="utf=8") as file:
        client_operations = json.load(file)
    execute = []
    for item in client_operations:
        execute.append(item)

    return execute


def get_executed_operations(lst: list) -> list:
    """
    Функция возвращает список выполненных операций.
    :param lst: Список операций.
    :return: Список выполненных операций.
    """
    executed_operations: list = []
    for item in lst:
        if "state" in item and item["state"] == "EXECUTED":
            executed_operations.append(item)

    return executed_operations


def sort_by_date(lst: list) -> list:
    """
    Функция сортирует список по дате в порядке убывания.
    :param lst: Список.
    :return: Отсортированный список в порядке убывания.
    """
    return sorted(lst, key=lambda x: x["date"], reverse=True)


def print_five_operations(lst: list) -> list:
    """
    Функция возвращает 5 последних операций.
    :param lst: Список выполненных операций.
    :return: Список 5 последних выполненных операций.
    """
    five_operation = lst[:5]

    return five_operation


def get_id_info(lst: list, oid: int) -> list:
    """
    Функция возвращает список с информацией об операциях по их id
    :param lst: Список операций.
    :param oid: Идентификатор операции.
    :return: Список с информацией по операциям
    """
    operation = lst[oid]
    operation_id = operation["id"]
    id_info = []
    for oper in lst:
        if oper["id"] == operation_id:
            id_info.append(oper)

    return id_info


def get_description(data: list) -> list:
    """
    Функция возвращает описание операции
    :param data: Список.
    :return:Элемент списка(словарь) по ключу "description"
    """
    return data[0]["description"]


def get_date(data: list) -> str:
    """
    Функция возвращает дату в формате "%Y-%m-%d"
    :param data: Список.
    :return: Строка.
    """
    date = data[0]["date"]
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


def get_to(accounts: list) -> str:
    """
    Функция возвращает номер счета в формате: Счет **ХХХХ
    :param accounts: Список.
    :return: Строка.
    """
    for account in accounts:
        to = account["to"]
    last_four = to[-4:]
    formatted = f"Счет **{last_four}"
    return formatted


def get_amount(transactions: list) -> list:
    """
    Функция возвращает кол-во переведенных средств.
    :param transactions: Список.
    :return: Список переводов по операциям.
    """
    amounts = []
    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError("Введенный параметр не является списком")
        if "operationAmount" in transaction and isinstance(transaction["operationAmount"], dict) and "amount" in transaction["operationAmount"]:
            amounts.append(float(transaction["operationAmount"]["amount"]))

        for i in amounts:
            return i


def get_from(transactions: list) -> str:
    """
    Функция возвращает счет отправителя в следующем формате: СЧЕТ(название карты) ХХХХ ХХ** **** ХХХХ
    :param transaction: Список.
    :return: Строка с счетом отправителя.
    """
    from_list = []

    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise TypeError("Введенный параметр не является списком")
        if "from" in transaction:
            from_list.append(transaction["from"])
    result = ""
    for i in from_list:
        words = i.split()
        for word in words:
            if any(char.isdigit() for char in word) and len(word) >= 16 and len(word) <= 19:
                result += word[:4] + " " + word[4:6] + "**" + " " + "****" + " " + word[-4:] + " "
            elif word.isalpha() or word.isspace():
                result += word + " "
    return result.strip()