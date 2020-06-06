from random import choice, sample
from typing import Optional

from .utilities import get_words_from_data_file


def get_random_name(count: Optional[int] = None,
                    gender: Optional[str] = None) -> str or list:
    '''
    Returns a random first name.

    Args:
        count (int, optional): The number of names to be
            generated. Defaults to None.
        gender (str): Specifies the name of which gender
            will be generated. Defaults to None.

    Returns:
        str: A random first name (if `count` is None).
        list: A list of random first names (if `count` is not None).

    Examples:
        >>> import randword as rw

        >>> rw.get_random_name()
        'Ethelred'

        >>> rw.get_random_name(gender='m')
        'Elden'

        >>> rw.get_random_name(gender='f')
        'Julee'

        >>> rw.get_random_name(count=4)
        ['Claudie', 'Trisha', 'Griffith', 'Annamarie']

        >>> rw.get_random_name(4, 'm')
        ['Helmuth', 'Collins', 'Ulrich', 'Zebedee']
    '''
    if gender == 'm':
        names = get_words_from_data_file('names/', 'male_names')
    elif gender == 'f':
        names = get_words_from_data_file('names/', 'female_names')
    else:
        male_names = get_words_from_data_file('names/', 'male_names')
        female_names = get_words_from_data_file('names/', 'female_names')
        names = male_names + female_names

    if count:
        return sample(names, count)
    else:
        return choice(names)


def get_random_surname(count: Optional[int] = None):
    '''
    Returns a random surname (or last name).

    Args:
        count (int, optional): The number of surnames to be
            generated. Defaults to None.

    Returns:
        str: A random surname (if `count` is None).
        list: A list of surnames (if `count` is not None).

    Examples:
        >>> import randword as rw

        >>> rw.get_random_surname()
        'Quicksall'

        >>> rw.get_random_surname(4)
        ['Shahan', 'Eickhoff', 'Akamiro', 'Giovanelli']
    '''
    surnames = get_words_from_data_file('names/', 'surnames')

    if count:
        return sample(surnames, count)
    else:
        return choice(surnames)


def get_random_fullname(count: Optional[int] = None,
                        gender: Optional[str] = None):
    '''
    Returns a random fullname.

    Args:
        count (int, optional): The number of fullnames to be
            generated. Defaults to None.
        gender (str): Specifies the fullname of which gender
            will be generated. Defaults to None.

    Returns:
        str: A random fullname (if `count` is None).
        list: A list of random fullnames (if `count` is not None).

    Examples:
        >>> import randword as rw

        >>> rw.get_random_fullname()
        'Charmane Bitzel'

        >>> rw.get_random_fullname(gender='m')
        'Nevin Mcnaught'

        >>> rw.get_random_fullname(gender='f')
        'Sophia Comans'

        >>> rw.get_random_fullname(count=2)
        ['Annetta Tiso', 'Babette Velazquez']

        >>> rw.get_random_fullname(2, 'm')
        ['Thaxter Vanhofwegen', 'Timmie Coray']
    '''
    if gender == 'm':
        names = get_words_from_data_file('names/', 'male_names')
    elif gender == 'f':
        names = get_words_from_data_file('names/', 'female_names')
    else:
        male_names = get_words_from_data_file('names/', 'male_names')
        female_names = get_words_from_data_file('names/', 'female_names')
        names = male_names + female_names

    surnames = get_words_from_data_file('names/', 'surnames')

    if count:
        fullnames = []
        random_names = sample(names, count)
        random_surnames = sample(surnames, count)

        for name, surname in zip(random_names, random_surnames):
            fullnames.append(f'{name} {surname}')

        return fullnames
    else:
        return f'{choice(names)} {choice(surnames)}'


if __name__ == '__main__':
    print(get_random_name())
    print(get_random_surname())
    print(get_random_fullname())
