from string import ascii_letters, digits
from random import choice
from typing import Optional, List, Union


def sequence(count: Optional[int] = None,
             length: int = 8) -> Union[str, List[str]]:
    '''Returns a random sequence consisting of ASCII symbols and digits or a list of a random sequences
    :param count: The number of sequences to be generated, defaults to `None`
    :type count: int, optional
    :param length: The length of the sequence, defaults to `8`
    :type length: int, optional
    :returns: A random sequence if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    chars = ascii_letters + digits

    if count:
        sequences = []
        for _ in range(count):
            sequences.append(''.join(choice(chars) for _ in range(length)))
        return sequences
    else:
        return ''.join(choice(chars) for _ in range(length))


def letter(count: Optional[int] = None) -> Union[str, List[str]]:
    '''Returns a random ASCII letter or a list of them
    :param count: The number of letters to be generated, defaults to `None`
    :type count: int, optional
    :returns: A random ASCII letter if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    if count:
        letters = []
        for _ in range(count):
            letters.append(choice(ascii_letters))
        return letters
    else:
        return choice(ascii_letters)


def digit(count: Optional[int] = None) -> Union[str, List[str]]:
    '''
    Returns a random digit.
    :param count: The number of digits to be generated, defaults to `None`
    :type count: int, optional
    :returns: A random digit if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    if count:
        digits_lst = []
        for _ in range(count):
            digits_lst.append(choice(digits))
        return digits_lst
    else:
        return choice(digits)


if __name__ == '__main__':
    print(sequence())
    print(letter())
    print(digit())
