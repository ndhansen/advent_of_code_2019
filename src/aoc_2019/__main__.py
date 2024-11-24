import argparse
import sys
from importlib.resources import files
from types import FrameType
from typing import Any

from aoc import puzzle
from rich.console import Console
from rich.pretty import pprint

from aoc_2019 import day_2, day_3, day_4, day_5, day_6, day_8

parser = argparse.ArgumentParser(prog="AOC", description="Advent of Code")
parser.add_argument("day", help="The day to run.")
parser.add_argument(
    "-t", "--test", action="store_true", help="Whether to use the test or real input."
)
parser.add_argument(
    "-w",
    "--watch",
    action="store_true",
    help="Watch for updates and print all output live",
)

args = parser.parse_args()

# Get the file contents
filename = "test.txt" if args.test else "input.txt"
path = files("aoc_2019.inputs") / args.day / filename
puzzle_input = puzzle.get_puzzle_input(path, test=args.test)

match args.day:
    case "day_2":
        part_1 = day_2.part_1
        part_2 = day_2.part_2
    case "day_3":
        part_1 = day_3.part_1
        part_2 = day_3.part_2
    case "day_4":
        part_1 = day_4.part_1
        part_2 = day_4.part_2
    case "day_5":
        part_1 = day_5.part_1
        part_2 = day_5.part_2
    case "day_6":
        part_1 = day_6.part_1
        part_2 = day_6.part_2
    case "day_8":
        part_1 = day_8.part_1
        part_2 = day_8.part_2
    case _:
        raise ValueError("Unknown day!")


def trace_function(frame: FrameType, event: str, arg: Any):
    if event == "return" and frame.f_code.co_name in ("part_1", "part_2"):
        pprint(
            dict(frame.f_locals),
            max_string=80,
            max_length=10,
            max_depth=3,
        )
    return trace_function


def run_puzzles() -> None:
    console = Console()
    print("Part 1:")
    try:
        print(part_1(puzzle_input))
    except Exception:
        console.print_exception(show_locals=True)
    print("Part 2:")
    try:
        print(part_2(puzzle_input))
    except Exception:
        console.print_exception(show_locals=True)


if args.watch:
    sys.settrace(trace_function)
    run_puzzles()
    sys.settrace(None)
else:
    run_puzzles()
