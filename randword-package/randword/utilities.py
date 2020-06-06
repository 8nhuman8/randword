from pkg_resources import resource_filename


def get_words_from_data_file(folder: str, filename: str) -> list:
    words = []
    filepath = resource_filename('randword', 'data/') + f'{folder}{filename}.txt'

    with open(filepath, 'r') as pos_file:
        pos_words = pos_file.readlines()
        words.extend(pos_words)

    return [word.rstrip() for word in words]
