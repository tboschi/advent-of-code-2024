import sys

from .utils import create_day, get_parser, solve_day


def main(args):
    solve_day(args.day, args.part)


if __name__ == "__main__":
    args = get_parser().parse_args()
    sys.exit(main(args))
