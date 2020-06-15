from pkg_resources import resource_filename
from typing import List
from pathlib import Path


def get_data(folder: str, filename: str) -> List[str]:
    words = []
    data_path = Path(resource_filename('randword', 'data'))
    filepath = data_path / folder / f'{filename}.txt'

    with open(filepath, 'r') as pos_file:
        pos_words = pos_file.readlines()
        words.extend(pos_words)

    return [word.rstrip() for word in words]
