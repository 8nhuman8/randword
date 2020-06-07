from string import ascii_letters, digits
from random import choice


def sequence(length: int = 8) -> str:
    '''
    Returns a random sequence consisting of ASCII symbols and digits.

    Args:
        length (int): The length of the sequence. Defaults to 8.

    Returns:
        str: The sequence.

    Example:
        >>> import randword as rw

        >>> rw.sequence():
        '8OOBn9XN'
    '''
    chars = ascii_letters + digits
    return ''.join(choice(chars) for _ in range(length))


def letter() -> str:
    '''
    Returns a random ASCII letter.

    Returns:
        str: An ASCII letter.

    Example:
        >>> import randword as rw

        >>> rw.letter():
        'Q'
    '''
    return choice(ascii_letters)


def digit() -> str:
    '''
    Returns a random digit.

    Returns:
        str: A digit.

    Example:
        >>> import randword as rw

        >>> rw.digit():
        '8'
    '''
    return choice(digits)


if __name__ == '__main__':
    print(sequence())
    print(letter())
    print(digit())
