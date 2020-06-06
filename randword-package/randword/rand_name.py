from random import choice, sample
from typing import Optional

from .utilities import get_words_from_data_file


def get_random_name(count: Optional[int] = None,
                    gender: Optional[str] = None):
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
    surnames = get_words_from_data_file('names/', 'surnames')

    if count:
        return sample(surnames, count)
    else:
        return choice(surnames)


def get_random_fullname(count: Optional[int] = None,
                        gender: Optional[str] = None):
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
