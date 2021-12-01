def name_and_phone_number():
    your_name = input("What's your name?")
    your_number = input("What's your phone number?")
    return f"Hello, ?, is ? your phone number?"


def what_type_does_input_return():
    your_favorite_number = input("What's your favorite number?")
    return type(your_favorite_number)


def add_your_two_favorite_numbers():
    favorite_number = input("What's your favorite number?")
    second_favorite_number = input("What's your second favorite number?")
    return f"The sum of your favorite numbers is {favorite_number + second_favorite_number}"