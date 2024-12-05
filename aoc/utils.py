import argparse
import importlib
import os
from pathlib import Path

PathType = str | os.PathLike


def generate_part(day: int, part: int) -> str:
    doc = f'""" Day {day} - part {part} """'
    return (
        doc
        + """

def solve(problem: list[str]) -> int:
    return 0


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = \"\"\"
\"\"\"
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
"""
    )


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="AOC 2024")
    parser.add_argument("day", type=int, help="the day to solve")
    parser.add_argument("--part", type=int, help="solve just the specified part")
    parser.add_argument(
        "--make", action="store_true", help="create a day folder from the template"
    )
    return parser


def read_from_file(path: PathType) -> list[str]:
    """Read a file into a list of lines"""
    with open(path) as file:
        data = file.read()
    return read_from_string(data)


def read_from_string(test: str) -> list[str]:
    """Split a test string into a list of lines"""
    return [clean_line for line in test.splitlines() if (clean_line := line.strip())]


def parse_list(data: str) -> list[int]:
    return [int(d) for d in data.split(",")]


def solve_day_part(day: int, part: int):
    solver = importlib.import_module(f"day{day:02}.part{part}")
    assert solver.__file__ is not None
    problem_file = Path(solver.__file__).parent / "input"
    problem = read_from_file(problem_file)
    print(f"Day {day} / part {part} -- solution is {solver.solve(problem)}")


def solve_day(day: int, part: int | None = None):
    if part is None:
        solve_day_part(day, 1)
        solve_day_part(day, 2)
    else:
        solve_day_part(day, part)


def create_day(day: int):
    path = Path(f"day{day:02}")
    print(path)
    if path.is_dir():
        print(f"{day} directory already exists")
        return

    path.mkdir()
    (path / "part1.py").write_text(generate_part(day, 1))
    (path / "part2.py").write_text(generate_part(day, 2))
