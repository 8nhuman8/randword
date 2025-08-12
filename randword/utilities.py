from typing import List
import importlib.resources


def get_data(folder: str, filename: str) -> List[str]:
    words = []

    with importlib.resources.path('randword', 'data') as data_path:
        filepath = data_path / folder / f'{filename}.txt'

        with open(filepath, 'r', encoding='utf-8') as pos_file:
            pos_words = pos_file.readlines()
            words.extend(pos_words)

    return [word.rstrip() for word in words]
