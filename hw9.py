ADDRESSBOOK = {}


def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
    return inner


@input_error
def add_handler(data):  # Функції обробники команд
    name = data[0].title()
    phone = data[1]
    email = data[3]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "Hello"


def command_parser(raw_str: str):  # Парсер команд
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if elements[0].lower() in value:
            return key, elements[1:]





COMMANDS = {
    add_handler: ["add", "додай", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"]
}


# @input_error
def main():  # Цикл запит-відповідь.
    while True:
        user_input = input(">>> ")  # add Vlad 0987009090
        if not user_input:
            continue
        func, data = command_parser(user_input)
        result = func(data)
        print(result)
        if func == exit_handler:
            break
        print(ADDRESSBOOK)


if __name__ == "__main__":
    main()
