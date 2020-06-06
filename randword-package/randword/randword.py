from pkg_resources import resource_filename
from random import choice, sample


''' From now on abbreviation "pos" means "part of speech" '''


def get_path_to_pos_file(part_of_speech: str) -> str:
    '''Returns the path to a file with words of a specific part of speech.

    Args:
        part_of_speech (str): The abbreviated name of the part of speech.

    Returns:
        str: The absolute path to the file.
    '''
    return resource_filename('randword', 'words/') + f'{part_of_speech}.txt'


def get_random_word(include_pos: list or None = None,
                    exclude_pos: list or None = None,
                    word_len: int or None = None,
                    min_word_len: int = 1,
                    max_word_len: int or None = None,
                    starts_with: str or None = None,
                    ends_with: str or None = None,
                    pattern: str or None = None) -> str:
    '''Returns a random English word.

    Args:
        include_pos (list of str or None): List of parts of speech that will be
            included in the generation. Deafults to None.
        exclude_pos (list of str or None): List of parts of speech that will be
            excluded in the generation. Deafults to None.
        word_len (int or None): Specifies the length of a word. Ignores the
            `min_word_len` and `max_word_len` parameters. Default to None.
        min_word_len (int): The minimum word length. Defaults to 1.
        max_word_len (int or None): The maximum word length. Defaults to None.
        starts_with (str or None): The pattern with which
            the word begins. Defaults to None.
        ends_with (str or None): The pattern with which
            the word ends. Defaults to None.
        pattern (str or None): The pattern that should be
            contained in the word. Defaults to None.

    Returns:
        str: A random English word.

    Raises:
        IndexError: If the word was not found.

    Examples:
        >>> import randword

        >>> randword.get_random_word()
        'concession'

        >>> randword.get_random_word(include_pos=['adj'])
        'accentual'

        >>> randword.get_random_word(include_pos=['adj', 'verb'])
        'immaterialize'

        >>> randword.get_random_word(exclude_pos=['adj', 'adv', 'noun', 'pron', 'verb'])
        'even if'

        >>> randword.get_random_word(min_word_len=20)
        'magnetic line of force'

        >>> randword.get_random_word(max_word_len=3)
        'use'

        >>> randword.get_random_word(min_word_len=4, max_word_len=5)
        'Sepia'

        >>> randword.get_random_word(word_len=5)
        'buggy'

        >>> randword.get_random_word(starts_with="ly")
        'lymphopoiesis'

        >>> randword.get_random_word(ends_with="en")
        'ten'

        >>> randword.get_random_word(starts_with="un", ends_with="e")
        'untouchable'

        >>> randword.get_random_word(pattern="ten")
        'finiteness'

        >>> randword.get_random_word(starts_with="e", ends_with="n", pattern="non")
        'enigma canon'
    '''
    if not include_pos:
        include_pos = ['adj', 'adv', 'conj', 'interj', 'noun', 'prep', 'pron', 'verb']

    if exclude_pos:
        parts_of_speech = list(set(include_pos) - set(exclude_pos))
    else:
        parts_of_speech = include_pos

    words = []
    for part_of_speech in parts_of_speech:
        pos_file_path = get_path_to_pos_file(part_of_speech)
        with open(pos_file_path, 'r') as pos_file:
            pos_words = pos_file.readlines()
            words.extend(pos_words)
    words = [word.rstrip() for word in words]

    if max_word_len:
        filtered_words = list(filter(lambda word: min_word_len <= len(word) <= max_word_len, words))
    else:
        filtered_words = list(filter(lambda word: min_word_len <= len(word), words))

    if word_len:
        filtered_words = list(filter(lambda word: word_len == len(word), words))

    if starts_with:
        filtered_words = list(filter(lambda word: word.startswith(starts_with), filtered_words))
    if ends_with:
        filtered_words = list(filter(lambda word: word.endswith(ends_with), filtered_words))
    if pattern:
        filtered_words = list(filter(lambda word: pattern in word, filtered_words))

    if not filtered_words:
        raise IndexError('The word was not found')

    return choice(filtered_words)


def get_random_words(words_count: int,
                     include_pos: list or None = None,
                     exclude_pos: list or None = None,
                     word_len: int or None = None,
                     min_word_len: int = 1,
                     max_word_len: int or None = None,
                     starts_with: str or None = None,
                     ends_with: str or None = None,
                     pattern: str or None = None) -> list:
    '''Returns a random English word.

    Args:
        words_count (int): 
        include_pos (list of str or None): List of parts of speech that will be
            included in the generation. Deafults to None.
        exclude_pos (list of str or None): List of parts of speech that will be
            excluded in the generation. Deafults to None.
        word_len (int or None): Specifies the length of a word. Ignores the
            `min_word_len` and `max_word_len` parameters. Default to None.
        min_word_len (int): The minimum word length. Defaults to 1.
        max_word_len (int or None): The maximum word length. Defaults to None.
        starts_with (str or None): The pattern with which
            the word begins. Defaults to None.
        ends_with (str or None): The pattern with which
            the word ends. Defaults to None.
        pattern (str or None): The pattern that should be
            contained in the word. Defaults to None.

    Returns:
        list: A list of random English words.

    Raises:
        IndexError: If the desired number of words was not found.

    Examples:
        >>> import randword

        >>> randword.get_random_words(3)
        ['Mozambican', 'demythologization', 'incontestable']

        >>> randword.get_random_words(3, include_pos=['adj'])
        ['discriminable', 'excrescent', 'noncivilized']

        >>> randword.get_random_words(3, include_pos=['adj', 'verb'])
        ['Ptolemaic', 'masonic', 'tangled']

        >>> randword.get_random_words(4, exclude_pos=['adj', 'adv', 'noun', 'pron', 'verb'])
        ['beneath', 'now that', 'upon', 'yup']

        >>> randword.get_random_words(2, min_word_len=20)
        ['plasma thromboplastin antecedent', 'United States House of Representatives']

        >>> randword.get_random_words(5, max_word_len=3)
        ['say', 'Ofo', 'rag', 'act', 'N']

        >>> randword.get_random_words(3, min_word_len=4, max_word_len=5)
        ['alga', 'butch', 'nark']

        >>> randword.get_random_words(2, word_len=7)
        ['kinesis', 'outcrop']

        >>> randword.get_random_words(3, starts_with="ly")
        ['lysogeny', 'lymphoblastic leukemia', 'lyceum']

        >>> randword.get_random_words(3, ends_with="en")
        ['genus Pecten', 'Dinesen', 'Eigen']

        >>> randword.get_random_words(3, starts_with="un", ends_with="e")
        ['unchaste', 'undersize', 'unprotective']

        >>> randword.get_random_words(3, pattern="ten")
        ['lichtenoid eczema', 'potential unit', 'minuteness']

        >>> randword.get_random_words(2, starts_with="e", ends_with="n", pattern="non")
        ['enigma canon', 'epiphenomenon']
    '''
    if not include_pos:
        include_pos = ['adj', 'adv', 'conj', 'interj', 'noun', 'prep', 'pron', 'verb']

    if exclude_pos:
        parts_of_speech = list(set(include_pos) - set(exclude_pos))
    else:
        parts_of_speech = include_pos

    words = []
    for part_of_speech in parts_of_speech:
        pos_file_path = get_path_to_pos_file(part_of_speech)
        with open(pos_file_path, 'r') as pos_file:
            pos_words = pos_file.readlines()
            words.extend(pos_words)
    words = [word.rstrip() for word in words]

    if max_word_len:
        filtered_words = list(filter(lambda word: min_word_len <= len(word) <= max_word_len, words))
    else:
        filtered_words = list(filter(lambda word: min_word_len <= len(word), words))

    if word_len:
        filtered_words = list(filter(lambda word: word_len == len(word), words))

    if starts_with:
        filtered_words = list(filter(lambda word: word.startswith(starts_with), filtered_words))
    if ends_with:
        filtered_words = list(filter(lambda word: word.endswith(ends_with), filtered_words))
    if pattern:
        filtered_words = list(filter(lambda word: pattern in word, filtered_words))

    INDEX_ERROR_DESCRIPTION = 'The desired number of words was not found'

    if not filtered_words:
        raise IndexError(INDEX_ERROR_DESCRIPTION)

    try:
        final_words = sample(filtered_words, words_count)
    except ValueError:
        raise IndexError(INDEX_ERROR_DESCRIPTION)

    return final_words


if __name__ == "__main__":
    print(get_random_word())
    print(get_random_words(8))
