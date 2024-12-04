from .utils import get_parser, solve_day

if __name__ == "__main__":
    args = get_parser().parse_args()
    solve_day(args.day, args.part)
