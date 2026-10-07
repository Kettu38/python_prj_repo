#   1
def create_dict() -> dict:
    """Напишите функцию, которая создаёт словарь с ключами 'name', 'age', 'city' и произвольными значениями"""
    return {
        'name': 'Kettu',
        'age': 22,
        'city': 'Moscow'
    }

#   2
def find_value(items: dict, key):
    """Напишите функцию, которая принимает словарь и ключ, и возвращает значение по этому ключу или None, если ключ не найден"""
    return items.get(key)


#   3
def add_job_key(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и добавляет в него новый ключ 'job' со значением 'developer' """
    items['job'] = items.get('job', 'developer')
    return items

#   4
def remove_age_key(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и удаляет из него ключ 'age' """
    items.pop('age', None)
    return items

#   5
def is_key_exists(items: dict, key) -> bool:
    """Напишите функцию, которая принимает словарь и ключ, и проверяет, существует ли этот ключ в словаре"""
    return True if items.get(key) != None else False

#   6
def merge_dicts(items_1: dict, items_2: dict) -> dict:
    """Напишите функцию, которая принимает два словаря и объединяет их в один (при совпадении ключей используется значение из второго словаря)"""
    return items_1 | items_2

#   7
from copy import deepcopy

def create_deepcopy(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и создаёт его глубокую копию"""
    return deepcopy(items)

#   8
def plus_one(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и увеличивает все числовые значения в этом словаре на 1"""
    return {k: v+1 for k, v in items.items()}

#   9
def remove_all_items(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и удаляет из него все элементы"""
    return {}

#   10
def swap_keys_to_values(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и меняет местами ключи и значения (если значения уникальны)"""
    return {key: value for value, key in items.items()}

#   11
def listing_keys_and_values(items: dict) -> list:
    """Напишите функцию, которая принимает словарь и возвращает два списка: список всех ключей и список всех значений"""
    return [item[0] for item in items.items()], [item for item in items.values()]

#   12
def keys_equals_45(items: dict) -> list:
    """Напишите функцию, которая принимает словарь и находит все ключи, у которых значение равно 42"""
    return [item[0] for item in items.items() if item[1] == 45]

#   13
def sort_by_keys(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и сортирует его по ключам в алфавитном порядке"""
    return dict(sorted(items.items(), key= lambda item: item[0]))

#   14
from operator import itemgetter

def sort_by_values(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и сортирует его по значениям по возрастанию"""
    return dict(sorted(items.items(), key= itemgetter(1)))

#   15
def more_than_ten(items: dict) -> dict:
    """Напишите функцию, которая принимает словарь и возвращает новый словарь, содержащий только те элементы, где значение больше 10"""
    return dict(filter(lambda item: item[1] > 10, items.items()))

#   16
def dict_to_list_of_tuples(items: dict) -> list:
    """Напишите функцию, которая принимает словарь и преобразует его в список кортежей вида (ключ, значение)"""
    return items.items()

#   17
def symbol_frequensy(text: str) -> dict:
    """Напишите функцию, которая принимает строку и считает, сколько раз каждый символ встречается в этой строке"""
    result = {}
    for symbol in text:
        result[symbol] = result.get(symbol, 0) + 1
    return result

#   18
def dict_to_string(items: dict) -> str:
    """Напишите функцию, которая принимает словарь и преобразует его в строку формата "key: value, key1: value1" """
    result = ''
    for item in items.items():
        result += f'{item[0]}: {item[1]}'
        result += ', '

    return result[:-2]

#   19
def eject_c_value(items: dict = {'a': {'b': {'c': 2}}}) -> int:
    """Напишите функцию, которая извлекает значение по ключу 'c' из вложенного словаря my_amazing_dict = {'a': {'b': {'c': 2}}}"""
    return items['a']['b']['c']

#   20
def max_key(items: dict):
    """Напишите функцию, которая принимает словарь и находит ключ с максимальным значением"""
    return max(items.keys())

#   21
def values_are_squares_of_keys() -> dict:
    """Напишите функцию, которая создаёт словарь, где ключи — числа от 1 до 5, а значения — квадраты этих чисел"""
    return {k: k**2 for k in range(1, 6)}


