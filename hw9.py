ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
    return wrap


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "Hello"


@input_error
def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key(elements[1:])
    return "Unknown command"


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}


def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
