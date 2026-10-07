# Реши задания 2 способами: используя filter() и используя list comprehensions
d = {
        'name': 'Kettu',
        'age': 22,
        'city': 'Moscow'
    }

# 1. Отфильтровать чётные числа 
# Из списка [1, 2, 3, 4, 5, 6] оставить только чётные.
list_1 = [1, 2, 3, 4, 5, 6]

print( list(filter(lambda x: x % 2 == 0, list_1)) )
print( [item for item in list_1 if item % 2 == 0] )

# 2. Фильтрация по длине слова
# Из списка слов оставить только те, длина которых больше 4 символов.
list_2 = ['agent', 'spacer', 'namer', 'Bob', 'cola']

print( list(filter(lambda item: len(item) > 4, list_2)) )
print( [item for item in list_2 if len(item) > 4] ) 

# 3. Фильтрация положительных чисел
# Из списка чисел оставить только положительные.
list_3 = [1, 2, -5, -6, 4]

print( list(filter(lambda item: item >= 0, list_3)) )
print( [item for item in list_3 if item >= 0] ) 

# 4. Оставить строки, начинающиеся с заглавной буквы
# Например, ["apple", "Banana", "Cat"] → ["Banana", "Cat"].
list_4 = ["apple", "Banana", "Cat"]

print( list(filter(lambda item: item.istitle(), list_4)) )
print( [item for item in list_4 if item.istitle()] )

# 5. Фильтрация email-адресов по домену
# Из списка e-mail оставить только те, что оканчиваются на @gmail.com.
list_5 = ['abc@gmail.com', 'kettu@mail.ru', 'man_2@yahoo.com', 'godsaveusall@gmail.com']

print( list(filter(lambda item: item.endswith('@gmail.com'), list_5)) )
print( [item for item in list_5 if item.endswith('@gmail.com')] )

# 6. Оставить палиндромы
# Из списка строк оставить только те, которые читаются одинаково в обе стороны.
list_6 = ['aba', 'шалаш', 'apple', 'kek']

print( list(filter(lambda item: item == item[::-1], list_6)) )
print( [item for item in list_6 if item == item[::-1]] )

# 7. Удалить пустые строки
# Из списка строк удалить пустые ("" или " ").
list_7 = ['MMM', '', 'Press F', ' ', 'kk']

print( list(filter(lambda item: not(item.isspace() or item == ''), list_7)) )
print( [item for item in list_7 if not(item.isspace() or item == '')] )

#----------------------

# Реши задания 2 способами: используя map() и используя list comprehensions

# 1. Возвести все числа в квадрат
# [1, 2, 3, 4] → [1, 4, 9, 16]
list_8 = [1, 2, 3, 4]

print( list(map(lambda item: item**2, list_8)) )
print( [item**2 for item in list_8] )

# 2. Перевести все слова в верхний регистр
# ["cat", "dog"] → ["CAT", "DOG"].
list_9 = ["cat", "dog"]

print( list(map(lambda item: item.upper(), list_9)) )
print( [item.upper() for item in list_9] )

# 3. Преобразовать строки чисел в числа
# ["1", "2", "3"] → [1, 2, 3]
list_10 = ["1", "2", "3"]

print( list(map(lambda item: int(item), list_10 )))
print( [int(item) for item in list_10] )

# 4. Добавить префикс ко всем словам
# Добавить 'Mr. ' перед каждым именем: ["John", "Alex"] → ["Mr. John", "Mr. Alex"]
list_11 = ["John", "Alex"]

print( list(map(lambda item: "Mr. " + item, list_11)))
print( ["Mr. " + item for item in list_11] )

# 5. Посчитать длину каждого слова
# ["apple", "pear"] → [5, 4].
list_12 = ["apple", "pear", "kek"]

print( list(map(lambda item: len(item), list_12)) )
print( [len(item) for item in list_12] )

# 6. Округлить числа до 2 знаков
# [3.1415, 2.718, 1.618] → [3.14, 2.72, 1.62]
list_13 = [3.1415, 2.718, 1.618]

print( list(map(lambda item: round(item, 2), list_13)) )
print( [round(item, 2) for item in list_13] )

# 7. Преобразовать список дат в формат YYYY-MM
# Например, ["2025-10-17", "2023-03-01"] → ["2025-10", "2023-03"]
list_14 = ["2025-10-17", "2023-03-01"]

print( list(map(lambda item: item[:-3], list_14)) )
print( [item[:-3] for item in list_14] )


