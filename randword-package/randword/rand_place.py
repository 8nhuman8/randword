from random import choice, sample
from typing import Optional, List, Union

from .utilities import get_words_from_data_file


def country(count: Optional[int] = None) -> Union[str, List[str]]:
    '''
    Returns a random country.

    Args:
        count (int, optional): The number of countries to be
            generated. Defaults to None.

    Returns:
        str: A random country (if `count` is None).
        list of str: A list of countries
            (if `count` is not None).

    Examples:
        >>> import randword as rw

        >>> rw.country()
        'Romania'

        >>> rw.country(4)
        ['Lithuania', 'Ethiopia', 'Romania', 'Cyprus']
    '''
    countries = get_words_from_data_file('places', 'countries')

    if count:
        return sample(countries, count)
    else:
        return choice(countries)


def city(count: Optional[int] = None) -> Union[str, List[str]]:
    '''
    Returns a random city.

    Args:
        count (int, optional): The number of cities to be
            generated. Defaults to None.

    Returns:
        str: A random city (if `count` is None).
        list of str: A list of cities
            (if `count` is not None).

    Examples:
        >>> import randword as rw

        >>> rw.city()
        'Charlotte'

        >>> rw.city(4)
        ['Scottsdale', 'Jefferson', 'Vero Beach', 'Gainesville']
    '''
    cities = get_words_from_data_file('places', 'cities')

    if count:
        return sample(cities, count)
    else:
        return choice(cities)


if __name__ == '__main__':
    print(country())
    print(city(4))
