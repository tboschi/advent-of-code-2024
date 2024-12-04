import argparse
import importlib
import os
from pathlib import Path

PathType = str | os.PathLike


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="AOC 2024")
    parser.add_argument("day", type=int, help="the day to solve")
    parser.add_argument("--part", type=int, help="solve just the specified part")
    return parser


def read_from_file(path: PathType) -> list[str]:
    """Read a file into a list of lines"""
    with open(path) as file:
        data = file.read()
    return read_from_string(data)


def read_from_string(test: str) -> list[str]:
    """Split a test string into a list of lines"""
    return [clean_line for line in test.splitlines() if (clean_line := line.strip())]


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
