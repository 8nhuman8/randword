from random import choice, sample
from typing import Optional, List, Union

from .utilities import get_data


def country(count: Optional[int] = None) -> Union[str, List[str]]:
    '''
    Returns a random country or a list of a random countries

    Args:
        count (int, optional): The number of countries to be
            generated. Defaults to `None`

    Returns:
        Union[str, List[str]]: A random country if `count` is `None` or a list of countries if `count` is not `None`
    '''
    countries = get_data('places', 'countries')

    if count:
        return sample(countries, count)
    else:
        return choice(countries)


def city(count: Optional[int] = None) -> Union[str, List[str]]:
    '''
    Returns a random city or a list of them

    Args:
        count (int, optional): The number of cities to be
            generated. Defaults to `None`

    Returns:
        Union[str, List[str]]: A random city if `count` is `None` or a list of cities if `count` is not `None`
    '''
    cities = get_data('places', 'cities')

    if count:
        return sample(cities, count)
    else:
        return choice(cities)


if __name__ == '__main__':
    print(country())
    print(city())
