from random import choice, sample
from typing import Optional, List, Union

from .utilities import get_data


PARTS_OF_SPEECH = ['adj', 'adv', 'conj', 'interj', 'noun', 'prep', 'pron', 'verb']


def word(count: Optional[int] = None,
         include_pos: Optional[List[str]] = None,
         exclude_pos: Optional[List[str]] = None,
         word_len: Optional[int] = None,
         min_word_len: int = 1,
         max_word_len: Optional[int] = None,
         starts_with: Optional[str] = None,
         ends_with: Optional[str] = None,
         pattern: Optional[str] = None) -> Union[str, List[str]]:
    '''Returns a random English word or a list of words. Abbreviation "pos" means "part of speech"
    :param count: The number of words to be generated, defaults to `None`
    :type count: int, optional
    :param include_pos: List of parts of speech that will be included in the generation, defaults to `None`
    :type include_pos: list, optional
    :param exclude_pos: List of parts of speech that will be excluded in the generation, defaults to `None`
    :type exclude_pos: list, optional
    :param word_len: Specifies the length of a word. Ignores the `min_word_len` and `max_word_len` parameters, defaults to `None`
    :type word_len: int, optional
    :param min_word_len: The minimum word length, defaults to `1`
    :type min_word_len: int, optional
    :param max_word_len: The maximum word length, defaults to `None`
    :type max_word_len: int, optional
    :param starts_with: The pattern with which the word begins, defaults to `None`
    :type starts_with: str, optional
    :param ends_with: The pattern with which the word ends, defaults to `None`
    :type ends_with: str, optional
    :param pattern: The pattern that should be contained in the word, defaults to `None`
    :returns: A random English word if `count` is `None` or a list of them if `count` is not `None`
    :rtype: str, list

    :raises IndexError: If the word was not found or if the desired number of words was not found
    '''
    if not include_pos:
        include_pos = PARTS_OF_SPEECH

    if exclude_pos:
        parts_of_speech = list(set(include_pos) - set(exclude_pos))
    else:
        parts_of_speech = include_pos

    words = []
    for part_of_speech in parts_of_speech:
        pos_words = get_data('parts_of_speech', part_of_speech)
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
    print(word())
