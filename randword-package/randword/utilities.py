from pkg_resources import resource_filename
from typing import List


def get_words_from_data_file(folder: str, filename: str) -> List[str]:
    '''
    A function for getting the list of words of the specific data file by
    determining the absolute path of the file with help of `folder` and
    `filename` parameters.

    Args:
        folder (str): The folder of the 'data' folder.
        filename (str): The name of the desired file.

    Returns:
        list of str: The list of words of specific data file.
    '''
    words = []
    filepath = resource_filename('randword', 'data/') + f'{folder}/{filename}.txt'

    with open(filepath, 'r') as pos_file:
        pos_words = pos_file.readlines()
        words.extend(pos_words)

    return [word.rstrip() for word in words]
