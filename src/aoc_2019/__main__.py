import argparse
from importlib.resources import files

from aoc import puzzle

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

# if args.watch:

print("Part 1:")
print(part_1(puzzle_input))
print("Part 2:")
print(part_2(puzzle_input))
