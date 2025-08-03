CLI Usage
=========

``randword`` is a command-line interface (CLI) tool for generating random words, names, sequences, places, and more. It wraps the `randword` Python package into a convenient CLI utility.

Basic Usage
-----------

By default, running ``randword`` with ``word`` arguments will generate a random word:

.. code-block:: bash

    $ randword word
    concession

You can also pass arguments to refine the result:

.. code-block:: bash

    $ randword word -i adj
    accentual

    $ randword word -min 8 -s un -x e
    untouchable

Subcommands
-----------

The CLI supports multiple subcommands:

.. code-block:: bash

    randword <command> [options]

Available commands:

- ``word``: Generate random word(s)
- ``name``: Generate random name(s)
- ``surname``: Generate random surname(s)
- ``fullname``: Generate random full name(s)
- ``sequence``: Generate alphanumeric sequence(s)
- ``letter``: Generate random letter(s)
- ``digit``: Generate random digit(s)
- ``country``: Generate random country/countries
- ``city``: Generate random city/cities
- ``magic_8ball``: Ask a Magic 8-Ball style question
- ``flip_coin``: Flip a coin

Command Details
---------------

**word**

.. code-block:: bash

    randword word [count] [options]

Options:

- ``-i``, ``--include_pos``: Include parts of speech (e.g. adj, verb)
- ``-e``, ``--exclude_pos``: Exclude parts of speech
- ``-min``, ``--min_word_len``: Minimum word length
- ``-max``, ``--max_word_len``: Maximum word length
- ``-l``, ``--word_len``: Exact word length
- ``-s``, ``--starts_with``: Start with given prefix
- ``-x``, ``--ends_with``: End with given suffix
- ``-p``, ``--pattern``: Match given substring pattern

Example:

.. code-block:: bash

    randword word 3 -i adj verb -s re -min 5

**name**

.. code-block:: bash

    randword name [count] [-g m|f]

**surname**

.. code-block:: bash

    randword surname [count]

**fullname**

.. code-block:: bash

    randword fullname [count] [-g m|f]

**sequence**

.. code-block:: bash

    randword sequence [count] [length]

**letter**

.. code-block:: bash

    randword letter [count]

**digit**

.. code-block:: bash

    randword digit [count]

**country**

.. code-block:: bash

    randword country [count]

**city**

.. code-block:: bash

    randword city [count]

**magic_8ball**

.. code-block:: bash

    randword magic_8ball

You will be prompted to type a yes/no question.

**flip_coin**

.. code-block:: bash

    randword flip_coin

Returns ``True`` for heads or ``False`` for tails.

Help
----

For help with any subcommand:

.. code-block:: bash

    randword <command> -h

Example:

.. code-block:: bash

    randword word -h
