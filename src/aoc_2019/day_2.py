import itertools
from typing import Any

from aoc_2019.utils.contents import PuzzleInput


def run_program(program: list[int]) -> int:
    numbers = program.copy()

    idx = 0
    while True:
        operation = numbers[idx]
        in_1 = numbers[idx + 1]
        in_2 = numbers[idx + 2]
        out = numbers[idx + 3]

        match operation:
            case 1:
                numbers[out] = numbers[in_1] + numbers[in_2]
            case 2:
                numbers[out] = numbers[in_1] * numbers[in_2]
            case 99:
                break
            case _:
                msg = "Operator not recognized."
                raise ValueError(msg)

        idx += 4

    return numbers[0]


def part_1(puzzle: PuzzleInput) -> int:
    numbers = [int(x) for x in puzzle.raw.split(",")]

    if puzzle.test is False:
        numbers[1] = 12
        numbers[2] = 2

    return run_program(numbers)


def part_2(puzzle: PuzzleInput) -> Any:
    targetted = 19690720
    numbers = [int(x) for x in puzzle.raw.split(",")]

    for noun, verb in itertools.product(range(100), repeat=2):
        numbers[1] = noun
        numbers[2] = verb

        if run_program(numbers) == targetted:
            return (100 * noun) + verb
