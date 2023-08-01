"""
Есть две строки в разных кодировках - "utf-8" и "utf-16". Нам необходимо понять, равны ли строки между собой.

Реализуйте функцию is_equal_string(utf8_string, utf16_string), которая возвращает True, если строки равны между собой,
и False — если нет.
"""


def is_equal_string(utf8_string: bytes, utf16_string: bytes):
    decode_utf8_string = utf8_string.decode("utf-8")
    decode_utf16_string = utf16_string.decode("utf-16")
    # if decode_utf16_string == decode_utf8_string:
    #     return True
    # else:
    #     return False
    return decode_utf16_string == decode_utf8_string

