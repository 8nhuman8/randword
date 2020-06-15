from string import ascii_letters, digits
from random import choice
from typing import Optional, List, Union


def sequence(count: Optional[int] = None,
             length: int = 8) -> Union[str, List[str]]:
    '''
    Returns a random sequence consisting of ASCII symbols and digits
    or a list of a random sequences.

    Args:
        count (int, optional): The number of sequances to be
            generated. Defaults to None.
        length (int): The length of the sequence. Defaults to 8.

    Returns:
        str: The sequence (if `count` is None).
        list of str: A list of sequences (if `count` is not None).

    Example:
        >>> import randword as rw

        >>> rw.sequence()
        '8OOBn9XN'

        >>> rw.sequence(5)
        ['hcre1hlC', 'jXTIqVAU', '6BwH7sUM', '2nAvHVh8', '6OANP6dO']

        >>> rw.sequence(5, 3)
        ['Tdv', '8Q0', 'HKG', 'K7X', 'Rwi']
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
    '''
    Returns a random ASCII letter or a list of them.

    Args:
        count (int, optional): The number of letters to be
            generated. Defaults to None.

    Returns:
        str: An ASCII letter (if `count` is None).
        list of str: A list of letters (if `count` is not None).

    Example:
        >>> import randword as rw

        >>> rw.letter()
        'Q'

        >>> rw.letter(10)
        ['D', 'M', 'N', 'j', 'h', 't', 'L', 'H', 'X', 'p']
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

    Args:
        count (int, optional): The number of digits to be
            generated. Defaults to None.

    Returns:
        str: A single digigt (if `count` is None).
        list of str: A list of digits (if `count` is not None).

    Example:
        >>> import randword as rw

        >>> rw.digit()
        '8'

        >>> rw.digit(10)
        ['1', '3', '6', '7', '5', '9', '4', '8', '2', '0']
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
