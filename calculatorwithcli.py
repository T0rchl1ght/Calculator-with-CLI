import argparse


def main():
    """Main entrypoint of cli."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # first command
    add = subparsers.add_parser("add")
    add.add_argument("numbers", nargs="+", type=int)
    # second command
    sub = subparsers.add_parser('subtract')
    sub.add_argument('numbers', nargs='+', type=int)

    args = parser.parse_args()
    if args.command == 'add':
        result = sum(args.numbers)
    print(f"The some of {args.numbers} is {result}")
    elif args.command == 'subtract':
    first, *rest = args.numbers
    result = first - sum(rest)
    print(f"The difference of {args.numbers} is {result}.")
    else:
    parser.print_help()


if __name__ == "__main__":
    main()