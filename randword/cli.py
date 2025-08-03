import argparse

from randword import (
    word,
    name,
    surname,
    fullname,
    sequence,
    letter,
    digit,
    country,
    city,
    magic_8ball,
    flip_coin,
)


def main():
    parser = argparse.ArgumentParser(description="CLI for randword package")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # === word ===
    word_parser = subparsers.add_parser("word", help="Generate random word(s)")
    word_parser.add_argument(
        "count", nargs="?", type=int, default=None, help="Number of words to generate"
    )
    word_parser.add_argument(
        "-i",
        "--include_pos",
        nargs="+",
        help="Parts of speech to include (e.g. adj verb)",
    )
    word_parser.add_argument(
        "-e", "--exclude_pos", nargs="+", help="Parts of speech to exclude (e.g. noun)"
    )
    word_parser.add_argument(
        "-min", "--min_word_len", type=int, help="Minimum word length"
    )
    word_parser.add_argument(
        "-max", "--max_word_len", type=int, help="Maximum word length"
    )
    word_parser.add_argument("-l", "--word_len", type=int, help="Exact word length")
    word_parser.add_argument(
        "-s", "--starts_with", help="String the word should start with"
    )
    word_parser.add_argument(
        "-x", "--ends_with", help="String the word should end with"
    )
    word_parser.add_argument("-p", "--pattern", help="Pattern the word should contain")

    # === name ===
    name_parser = subparsers.add_parser("name", help="Generate random name(s)")
    name_parser.add_argument(
        "count", nargs="?", type=int, default=None, help="Number of names to generate"
    )
    name_parser.add_argument(
        "-g", "--gender", choices=["m", "f"], help="Gender of name (m or f)"
    )

    # === surname ===
    surname_parser = subparsers.add_parser("surname", help="Generate random surname(s)")
    surname_parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=None,
        help="Number of surnames to generate",
    )

    # === fullname ===
    fullname_parser = subparsers.add_parser(
        "fullname", help="Generate random full name(s)"
    )
    fullname_parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=None,
        help="Number of full names to generate",
    )
    fullname_parser.add_argument(
        "-g", "--gender", choices=["m", "f"], help="Gender of full name (m or f)"
    )

    # === sequence ===
    sequence_parser = subparsers.add_parser(
        "sequence", help="Generate random alphanumeric sequence(s)"
    )
    sequence_parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=None,
        help="Number of sequences to generate",
    )
    sequence_parser.add_argument(
        "length", nargs="?", type=int, default=None, help="Length of each sequence"
    )

    # === letter ===
    letter_parser = subparsers.add_parser("letter", help="Generate random letter(s)")
    letter_parser.add_argument(
        "count", nargs="?", type=int, default=None, help="Number of letters to generate"
    )

    # === digit ===
    digit_parser = subparsers.add_parser("digit", help="Generate random digit(s)")
    digit_parser.add_argument(
        "count", nargs="?", type=int, default=None, help="Number of digits to generate"
    )

    # === country ===
    country_parser = subparsers.add_parser(
        "country", help="Generate random country/countries"
    )
    country_parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=None,
        help="Number of countries to generate",
    )

    # === city ===
    city_parser = subparsers.add_parser("city", help="Generate random city/cities")
    city_parser.add_argument(
        "count", nargs="?", type=int, default=None, help="Number of cities to generate"
    )

    # === magic_8ball ===
    subparsers.add_parser("magic_8ball", help="Ask the Magic 8-Ball a question")

    # === flip_coin ===
    subparsers.add_parser("flip_coin", help="Flip a coin (True=Heads, False=Tails)")

    # Default to "word" if no subcommand is given
    # if len(sys.argv) == 1 or sys.argv[1].startswith("-"):
    #     sys.argv.insert(1, "word")

    args = parser.parse_args()

    # === Dispatch Logic ===
    if args.command == "word":
        kwargs = {
            "include_pos": args.include_pos,
            "exclude_pos": args.exclude_pos,
            "min_word_len": args.min_word_len,
            "max_word_len": args.max_word_len,
            "word_len": args.word_len,
            "starts_with": args.starts_with,
            "ends_with": args.ends_with,
            "pattern": args.pattern,
        }
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        result = (
            word(args.count, **kwargs) if args.count is not None else word(**kwargs)
        )

    elif args.command == "name":
        result = (
            name(args.count, args.gender)
            if args.count is not None
            else name(gender=args.gender)
        )

    elif args.command == "surname":
        result = surname(args.count) if args.count else surname()

    elif args.command == "fullname":
        result = (
            fullname(args.count, args.gender)
            if args.count is not None
            else fullname(gender=args.gender)
        )

    elif args.command == "sequence":
        if args.count is not None and args.length is not None:
            result = sequence(args.count, args.length)
        elif args.count is not None:
            result = sequence(args.count)
        else:
            result = sequence()

    elif args.command == "letter":
        result = letter(args.count) if args.count else letter()

    elif args.command == "digit":
        result = digit(args.count) if args.count else digit()

    elif args.command == "country":
        result = country(args.count) if args.count else country()

    elif args.command == "city":
        result = city(args.count) if args.count else city()

    elif args.command == "magic_8ball":
        _ = magic_8ball()
        return

    elif args.command == "flip_coin":
        result = flip_coin()

    print(result)


if __name__ == "__main__":
    main()
