def add_handler(*args):  # Функції обробники команд
    return args


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "Hello"


def command_parser(raw_str: str):  # Парсер команд
    items = raw_str.split()
    for key, value in COMMANDS.items():
        


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        if not user_input:
            continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
