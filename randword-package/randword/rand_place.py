from random import choice, sample
from typing import Optional, List, Union

from .utilities import get_data


def country(count: Optional[int] = None) -> Union[str, List[str]]:
    '''Returns a random country or a list of a random countries
    :param count: The number of countries to be generated, defaults to `None`
    :type count: int, optional
    :returns: A random country if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    countries = get_data('places', 'countries')

    if count:
        return sample(countries, count)
    else:
        return choice(countries)


def city(count: Optional[int] = None) -> Union[str, List[str]]:
    '''Returns a random city or a list of them
    :param count: The number of cities to be generated, defaults to `None`
    :type count: int, optional
    :returns: A random city if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list
    '''
    cities = get_data('places', 'cities')

    if count:
        return sample(cities, count)
    else:
        return choice(cities)


if __name__ == '__main__':
    print(country())
    print(city())
