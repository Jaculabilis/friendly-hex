import argparse
import sys

import fhex.parse

def main():
    parser = argparse.ArgumentParser(
        description="Convert hex strings to and from human-readable strings.")
    parser.add_argument("-f", "--format", default="APNF")
    parser.add_argument("-x", "--hex", nargs="?", const="-",
        help="Hex code to translate to friendly string. If no value is" +
        " specified, read hex from stdin.")
    parser.add_argument("-s", "--string", nargs="?", const="-",
        help="Friendly string to translate to hex. If no value is specified," +
        " read string from stdin.")
    parser.add_argument("--titlecase", action="store_true",
        help="Titlecase friendly string output.")
    parser.add_argument("--hyphenate", action="store_true",
        help="Hyphenate friendly string output.")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    if args.verbose:
        print("friendly-hex", file=sys.stderr)
        print("  --format =", args.format, file=sys.stderr)
        print("  --hex =", args.hex, file=sys.stderr)
        print("  --string =", args.string, file=sys.stderr)
        print("  --titlecase =", args.titlecase, file=sys.stderr)
        print("  --hyphenate =", args.hyphenate, file=sys.stderr)
        print("  --verbose =", args.verbose, file=sys.stderr)
        print(file=sys.stderr)

    if args.hex is None and args.string is None:
        parser.error("One of --hex or --string is required.")

    if args.hex is not None and args.string is None:
        # Convert hex to friendly string
        if args.hex == "-":
            args.hex = sys.stdin.readline().strip()
            if args.verbose:
                print(f'Read "{args.hex}" from stdin', file=sys.stderr)

        words = fhex.parse.hex_to_friendly(args.hex, args.format)
        if args.titlecase:
            words = [word.title() for word in words]

        joiner = "-" if args.hyphenate else " "
        joined = joiner.join(words)

        print(joined)

    if args.hex is None and args.string is not None:
        # Convert friendly string to hex
        raise NotImplementedError()


if __name__ == "__main__":
    main()

