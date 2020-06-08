from random import choice, randrange, getrandbits
from time import sleep

from utilities import get_data


def magic_8ball() -> None:
    answers = get_data('other', 'magic_8ball_answers')

    def main() -> None:
        input('- Ask me a question:\n+ ')

        print('- Thinking...')
        sleep(randrange(0, 3))

        print(f'~ {choice(answers)}\n')

    while True:
        main()
        repeat = input('- Would you like to ask another question? [Y/N]\n+ ')
        if repeat.upper() != 'Y':
            print('- Come back if you have questions.')
            break


def flip_coin() -> bool:
    return bool(getrandbits(1))


if __name__ == '__main__':
    print(flip_coin())
