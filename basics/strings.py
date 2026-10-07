#   1
def merge_strings(str1: str, str2: str) -> str:
    """Напишите функцию, которая принимает две строки и возвращает их конкатенацию (объединение)"""
    return str1 + str2

#   2
def string_length(input_string: str) -> int:
    """Напишите функцию, которая при нимает строку и возвращает длину этой строки"""
    return len(input_string)

#   3
def repeat_string(text: str, counter: int) -> str:
    """Напишите функцию, которая принимает строку и повторяет эту строку n раз"""
    return text * counter

#   4
def first_n_last_symbol(text: str) -> str:
    """Напишите функцию, которая принимает строку и возвращает первый и последний символ этой строки"""
    return text[0] + text[-1]

#   5
def from_3rd_to_5th(text: str) -> str:
    """Напишите функцию, которая принимает строку и возвращает подстроку с 3-го по 5-й символ"""
    return text[2:5]

#   6
def counter_of_a(text: str) -> int:
    """Напишите функцию, которая принимает строку и считает, сколько раз символ 'a' встречается в этой строке"""
    return text.count('a')

#   7
def replace_space_to_underscore(text: str) -> str:
    """Напишите функцию, которая принимает строку и заменяет все пробелы в этой строке на "_" """
    return text.replace(' ', '_')

#   8
def reverce_string(text: str) -> str:
    """Напишите функцию, которая принимает строку и возвращает эту строку, перевёрнутую задом наперёд"""
    return text[::-1]

#   9
def up_stroke(text: str) -> str:
    """Напишите функцию, которая принимает строку и переводит её в верхний регистр"""
    return text.upper()

#   10
def make_title(text: str) -> str:
    """Напишите функцию, которая принимает строку и делает первую букву каждого слова в этой строке заглавной"""
    return text.title()

#   11
def strip_string(text: str) -> str:
    """Напишите функцию, которая принимает строку и удаляет лишние пробелы в начале и конце этой строки"""
    return text.strip()

#   12 
def is_palindrome(text: str) -> bool:
    """Напишите функцию, которая принимает строку и проверяет, является ли она палиндромом"""
    return text == text[::-1]

#   13
def is_digit(text: str) -> bool:
    """Напишите функцию, которая принимает строку и проверяет, состоит ли эта строка только из цифр"""
    return text.isdigit()

#   14
def is_alpha(text: str) -> bool:
    """Напишите функцию, которая принимает строку и проверяет, состоит ли эта строка только из букв"""
    return text.isalpha()

#   15
def starts_with(text: str) -> bool:
    """Напишите функцию, которая принимает строку и проверяет, начинается ли эта строка с "Hello" """
    return text.startswith('Hello')

#   16
def string_to_list(text: str) -> list:
    """Напишите функцию, которая принимает строку и разбивает её по пробелам, возвращая список слов"""
    return [word for word in text.split(' ')]

#   17
def list_to_string(list_of_words: list) -> str:
    """Напишите функцию, которая принимает список строк и объединяет его в одну строку через запятую"""
    return ','.join(list_of_words)

#   18
def represent_myself(name: str, age: int) -> str:
    """Напишите функцию, которая принимает имя и возраст, и подставляет их в строку "Меня зовут {name}, мне {age} лет" """ 
    return f"Меня зовут {name}, мне {age} лет"

#   19
def count_words(text: str) -> str:
    """Напишите функцию, которая принимает строку и считает количество слов в этой строке"""
    return len(text.split())

#   20
def count_symbols(text: str) -> dict:
    """Напишите функцию, которая принимает строку и возвращает словарь с количеством каждого символа в этой строке"""
    dict_of_symbols = {}
    for s in text:
        dict_of_symbols[s] = dict_of_symbols.get(s, 0) + 1
    
    return dict_of_symbols

#   21
def longest_word(text: str) -> str:
    """Напишите функцию, которая принимает строку и находит самое длинное слово в этой строке"""
    return str(sorted(text.split(), key= lambda x: len(x), reverse=True)[0])

    #^^^ Есть ощущение, что такую запись лучше разбивать ^^^

#   22
import random
def paswor_gen(password_length: int) -> str:
    """Напишите функцию, которая принимает число и генерирует случайный пароль заданной длины из букв, цифр и спецсимволов"""
    #Нужны символы с 33 по 122 (unicode, десятичная система)
    
    password = ''
    for s in range(password_length + 1):
        password += chr(random.randint(33, 122))
    
    return password

