"""
Вернемся к предыдущей задаче и выполним обратную задачу.
 Напишите рекурсивную функцию encode для кодирования списка или строки.
 В качестве аргумента функция принимает список ( например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"])
 или строку (например "XXXZZXXYYYZZ"). Функция должна вернуть закодированный список элементов
  (пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

"""

data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]


def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index += 1

    current = [data[0], index]
    print(current)
    return current + encode(data[index:len(data)])


print(encode(data))
