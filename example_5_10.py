"""
Напишите функцию find_word, которая принимает два параметра: первый text и второй word.
Функция выполняет поиск указанного слова word в тексте text с помощью функции search и возвращает словарь.
где
{ 'result': True, 'first_index': 34, 'last_index': 40, 'search_string': 'Python',
 'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
 and first released it in 1991 as Python 0.9.0.' }
result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию

Если совпадений не обнаружено:

{ 'result': False, 'first_index': None, 'last_index': None, 'search_string': 'python',
'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.' }
"""

"""
s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>

Щоб витягнути власне знайдене значення із age, можна скористатися його методом group

s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25
"""
import re


def find_word(text, word):
    result = re.search(word, text)
    if result:
        first_index = result.span()[0]
        last_index = result.span()[1]
        search_string = result.group()
        return {'result': True, 'first_index': first_index, 'last_index': last_index, 'search_string': search_string,
                'string': text}
    else:
        return {'result': False, 'first_index': None, 'last_index': None, 'search_string': word, 'string': text}
