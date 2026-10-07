#   1
def sum_list(items: list) -> float:
    """Напишите функцию, которая принимает список чисел и возвращает сумму всех чисел в этом списке"""
    return sum(items)

#   2
def  min_and_max(items: list) -> tuple:
    """Напишите функцию, которая принимает список и находит максимальный и минимальный элементы"""
    return min(items), max(items)

#   3
def average_of_list(items: list) -> float:
    """Напишите функцию, которая принимает список чисел и вычисляет среднее арифметическое элементов этого списка"""
    return sum(items) / len(items)

#   4
def list_len(items: list) -> int:
    """Напишите функцию, которая принимает список и возвращает его длину"""
    return len(items)

#   5
def reverse_list(items: list) -> list:
    """Напишите функцию, которая принимает список и разворачивает его в обратном порядке"""
    return items[::-1]

#   6
def remove_copies(items: list) -> list:
    """Напишите функцию, которая принимает список и удаляет из него повторяющиеся элементы, сохраняя порядок"""
    return list(dict.fromkeys(items))

#   7
def append_lists(list_1: list, list_2: list) -> list:
    """Напишите функцию, которая принимает два списка и соединяет их в один"""
    list_1.extend(list_2)
    return list_1

#   8
def insert_42(items: list) -> list:
    """Напишите функцию, которая принимает список и вставляет число 42 на позицию с индексом 3"""
    items.insert(3, 42)
    return items

#   9
def remove_fives(items: list[float]) -> list:
    """Напишите функцию, которая принимает список и удаляет из него все вхождения числа 5"""
    if 5 in items: items.remove(5)
    return items

#   10
def evens_only(items: list) -> list:
    """Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только чётные числа"""
    return [item for item in items if item % 2 == 0]

#   11
def how_many_apples(items: list) -> int:
    """Напишите функцию, которая принимает список и считает, сколько раз элемент 'apple' встречается в этом списке"""
    return items.count('apple')

#   12
def longer_than_3(items: list[str]):
    """Напишите функцию, которая принимает список строк и оставляет в этом списке только строки длиной больше 3 символов"""
    return [item for item in items if len(item) > 3]

#   13
def make_suqares(items: list) -> list:
    """Напишите функцию, которая принимает список чисел и создаёт новый список с квадратами элементов исходного списка"""
    return [item ** 2 for item in items]

#   14
def negatives_to_zero(items: list) -> list:
    """Напишите функцию, которая принимает список чисел и заменяет все отрицательные числа на 0"""
    return [item if item >= 0 else 0 for item in items]

#   15
def sort_by_len(items: list[str]) -> list:
    """Напишите функцию, которая принимает список строк и сортирует его по длине строк"""
    return sorted(items, key = lambda item: len(item))

#   16
def evens_odds_indexes(items: list) -> list:
    """Напишите функцию, которая принимает список и возвращает два списка: один с элементами на чётных индексах, другой — с элементами на нечётных"""
    evens = [item for i, item in enumerate(items) if i % 2 == 0]
    odds = [item for i, item in enumerate(items) if i % 2 != 0]
    return evens, odds

#   17
def intersections_only(items_1: list, items_2: list) -> list:
    """Напишите функцию, которая принимает два списка и возвращает список общих элементов"""
    return list(set(items_1) & set(items_2))

#   18
def elements_counter(items: list) -> dict:
    """Напишите функцию, которая принимает список и возвращает словарь, где ключ — элемент списка, а значение — количество его вхождений"""
    item_counts = {}
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1

    return item_counts

#   19
def list_offset(items: list, offset: int) -> list:
    """Напишите функцию, которая принимает список и число n, и сдвигает элементы списка на n позиций вправо"""
    result = [None for item in range(offset)]
    result.extend(items)
    return result

#   20
def remove_copies_2(items: list) -> list:
    """Напишите функцию, которая принимает список и удаляет из него все элементы, встречающиеся более одного раза"""
    return list(set(items))

