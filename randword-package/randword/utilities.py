from pkg_resources import resource_filename
from typing import List
from pathlib import Path


def get_data(folder: str, filename: str) -> List[str]:
    '''
    A function for getting the list of data of the specific file by
    determining the absolute path of the file with help of `folder` and
    `filename` parameters.

    Args:
        folder (str): The folder of the 'data' folder.
        filename (str): The name of the desired file.

    Returns:
        list of str: The list of words of specific data file.
    '''
    words = []
    data_path = Path(resource_filename('randword', 'data'))
    filepath = data_path / folder / f'{filename}.txt'

    with open(filepath, 'r') as pos_file:
        pos_words = pos_file.readlines()
        words.extend(pos_words)

    return [word.rstrip() for word in words]
