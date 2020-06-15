How to use
==========


**Random words**::

    >>> from randword import word

    >>> word()
    'concession'

    >>> word(include_pos=['adj'])
    'accentual'

    >>> word(include_pos=['adj', 'verb'])
    'immaterialize'

    >>> word(exclude_pos=['adj', 'adv', 'noun', 'pron', 'verb'])
    'even if'

    >>> word(min_word_len=20)
    'magnetic line of force'

    >>> word(max_word_len=3)
    'use'

    >>> word(min_word_len=4, max_word_len=5)
    'Sepia'

    >>> word(word_len=5)
    'buggy'

    >>> word(starts_with="ly")
    'lymphopoiesis'

    >>> word(ends_with="en")
    'ten'

    >>> word(starts_with="un", ends_with="e")
    'untouchable'

    >>> word(pattern="ten")
    'finiteness'

    >>> word(starts_with="e", ends_with="n", pattern="non")
    'enigma canon'

    >>> word(count=3)
    ['Mozambican', 'demythologization', 'incontestable']

    >>> word(3, include_pos=['adj'])
    ['discriminable', 'excrescent', 'noncivilized']

    >>> word(3, ['adj', 'verb'])
    ['Ptolemaic', 'masonic', 'tangled']

    >>> word(4, exclude_pos=['adj', 'adv', 'noun', 'pron', 'verb'])
    ['beneath', 'now that', 'upon', 'yup']

    >>> word(2, min_word_len=20)
    ['plasma thromboplastin antecedent',
    'United States House of Representatives']

    >>> word(count=5, max_word_len=3)
    ['say', 'Ofo', 'rag', 'act', 'N']

    >>> word(3, min_word_len=4, max_word_len=5)
    ['alga', 'butch', 'nark']

    >>> word(2, word_len=7)
    ['kinesis', 'outcrop']

    >>> word(3, starts_with="ly")
    ['lysogeny', 'lymphoblastic leukemia', 'lyceum']

    >>> word(3, ends_with="en")
    ['genus Pecten', 'Dinesen', 'Eigen']

    >>> word(3, starts_with="un", ends_with="e")
    ['unchaste', 'undersize', 'unprotective']

    >>> word(3, pattern="ten")
    ['lichtenoid eczema', 'potential unit', 'minuteness']

    >>> word(count=2, starts_with="e", ends_with="n", pattern="non")
    ['enigma canon', 'epiphenomenon']


**Random names**::

    >>> from randword import name, surname, fullname


    >>> name()
    'Ethelred'

    >>> name(gender='m')
    'Elden'

    >>> name(gender='f')
    'Julee'

    >>> name(count=4)
    ['Claudie', 'Trisha', 'Griffith', 'Annamarie']

    >>> name(4, 'm')
    ['Helmuth', 'Collins', 'Ulrich', 'Zebedee']


    >>> surname()
    'Quicksall'

    >>> surname(4)
    ['Shahan', 'Eickhoff', 'Akamiro', 'Giovanelli']


    >>> fullname()
    'Charmane Bitzel'

    >>> fullname(gender='m')
    'Nevin Mcnaught'

    >>> fullname(gender='f')
    'Sophia Comans'

    >>> fullname(count=2)
    ['Annetta Tiso', 'Babette Velazquez']

    >>> fullname(2, 'm')
    ['Thaxter Vanhofwegen', 'Timmie Coray']


**Random sequences, letters and digits**::

    >>> from randword import sequence, letter, digits


    >>> sequence()
    '8OOBn9XN'

    >>> sequence(5)
    ['hcre1hlC', 'jXTIqVAU', '6BwH7sUM', '2nAvHVh8', '6OANP6dO']

    >>> sequence(5, 3)
    ['Tdv', '8Q0', 'HKG', 'K7X', 'Rwi']


    >>> letter()
    'Q'

    >>> letter(10)
    ['D', 'M', 'N', 'j', 'h', 't', 'L', 'H', 'X', 'p']


    >>> digit()
    '8'

    >>> digit(10)
    ['1', '3', '6', '7', '5', '9', '4', '8', '2', '0']


**Random places**::

    >>> from randword import country, city


    >>> country()
    'Romania'

    >>> country(4)
    ['Lithuania', 'Ethiopia', 'Romania', 'Cyprus']


    >>> city()
    'Charlotte'

    >>> city(4)
    ['Scottsdale', 'Jefferson', 'Vero Beach', 'Gainesville']


**Some other random stuff**::

    >>> from randword import magic_8ball, flip_coin


    >>> magic_8ball()
    Ask me a question:
      Will the weather be good tomorrow?
    Thinking...
      Cannot predict now.

    Would you like to ask another question? [Y/N] n
    Come back if you have questions.


    >>> flip_coin()
    False
    >>> flip_coin()
    True
