from random import choice, sample
from typing import Optional, List

from .utilities import get_words_from_data_file


PARTS_OF_SPEECH = ['adj', 'adv', 'conj', 'interj', 'noun', 'prep', 'pron', 'verb']


''' Abbreviation "pos" means "part of speech" '''
def get_random_word(count: Optional[int] = None,
                    include_pos: Optional[List[str]] = None,
                    exclude_pos: Optional[List[str]] = None,
                    word_len: Optional[int] = None,
                    min_word_len: int = 1,
                    max_word_len: Optional[int] = None,
                    starts_with: Optional[str] = None,
                    ends_with: Optional[str] = None,
                    pattern: Optional[str] = None) -> str or list:
    '''
    Returns a random English word or a list of words.
    Abbreviation "pos" means "part of speech".

    Args:
        count (int, optional): The number of words to
            be generated. Defaults to None.
        include_pos (list of str, optional): List of parts of speech that will be
            included in the generation. Defaults to None.
        exclude_pos (list of str, optional): List of parts of speech that will be
            excluded in the generation. Defaults to None.
        word_len (int, optional): Specifies the length of a word. Ignores the
            `min_word_len` and `max_word_len` parameters. Defaults to None.
        min_word_len (int): The minimum word length. Defaults to 1.
        max_word_len (int, optional): The maximum word length. Defaults to None.
        starts_with (str, optional): The pattern with which
            the word begins. Defaults to None.
        ends_with (str, optional): The pattern with which
            the word ends. Defaults to None.
        pattern (str, optional): The pattern that should be
            contained in the word. Defaults to None.

    Returns:
        str: A random English word (if `words_count` is None).
        list: A list of random English words (if `words_count` is not None).

    Raises:
        IndexError: If the word was not found or if the
            desired number of words was not found.

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

        >>> randword.get_random_word(count=3)
        ['Mozambican', 'demythologization', 'incontestable']

        >>> randword.get_random_word(count=3, include_pos=['adj'])
        ['discriminable', 'excrescent', 'noncivilized']

        >>> randword.get_random_word(count=3, include_pos=['adj', 'verb'])
        ['Ptolemaic', 'masonic', 'tangled']

        >>> randword.get_random_word(count=4, exclude_pos=['adj', 'adv', 'noun', 'pron', 'verb'])
        ['beneath', 'now that', 'upon', 'yup']

        >>> randword.get_random_word(count=2, min_word_len=20)
        ['plasma thromboplastin antecedent', 'United States House of Representatives']

        >>> randword.get_random_word(count=5, max_word_len=3)
        ['say', 'Ofo', 'rag', 'act', 'N']

        >>> randword.get_random_word(count=3, min_word_len=4, max_word_len=5)
        ['alga', 'butch', 'nark']

        >>> randword.get_random_word(count=2, word_len=7)
        ['kinesis', 'outcrop']

        >>> randword.get_random_word(count=3, starts_with="ly")
        ['lysogeny', 'lymphoblastic leukemia', 'lyceum']

        >>> randword.get_random_word(count=3, ends_with="en")
        ['genus Pecten', 'Dinesen', 'Eigen']

        >>> randword.get_random_word(count=3, starts_with="un", ends_with="e")
        ['unchaste', 'undersize', 'unprotective']

        >>> randword.get_random_word(count=3, pattern="ten")
        ['lichtenoid eczema', 'potential unit', 'minuteness']

        >>> randword.get_random_word(count=2, starts_with="e", ends_with="n", pattern="non")
        ['enigma canon', 'epiphenomenon']
    '''
    if not include_pos:
        include_pos = PARTS_OF_SPEECH

    if exclude_pos:
        parts_of_speech = list(set(include_pos) - set(exclude_pos))
    else:
        parts_of_speech = include_pos

    words = []
    for part_of_speech in parts_of_speech:
        pos_words = get_words_from_data_file('parts_of_speech/', part_of_speech)
        words.extend(pos_words)

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

    if count:
        INDEX_ERROR_DESCRIPTION = 'The desired number of words was not found'

        if not filtered_words:
            raise IndexError(INDEX_ERROR_DESCRIPTION)

        try:
            final_words = sample(filtered_words, count)
        except ValueError:
            raise IndexError(INDEX_ERROR_DESCRIPTION)

        return final_words
    else:
        if not filtered_words:
            raise IndexError('The word was not found')

        return choice(filtered_words)


if __name__ == '__main__':
    print(get_random_word())
