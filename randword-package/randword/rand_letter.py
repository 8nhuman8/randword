from string import ascii_letters, ascii_lowercase, \
                   ascii_uppercase, digits
from random import choice


def get_random_sequence(length: int = 8) -> str:
    chars = ascii_letters + digits
    return ''.join(choice(chars) for _ in range(length))


def get_random_letter() -> str:
    return choice(ascii_letters)


def get_random_digit() -> str:
    return choice(digits)


if __name__ == '__main__':
    print(get_random_sequence())
    print(get_random_letter())
    print(get_random_digit())
