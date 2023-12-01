from typing import Any

import parse

from aoc_2019.utils.contents import PuzzleInput


def adjacent(num: int) -> bool:
    digits = str(num)
    for i in range(5):
        if digits[i] == digits[i + 1]:
            return True
    return False


def decreasing(num: int) -> bool:
    digits = str(num)
    last = digits[0]
    for i in range(1, 6):
        if int(digits[i]) < int(last):
            return True
        last = digits[i]
    return False


def count_passwords(start: int, end: int) -> int:
    working = 0
    for password in range(start, end + 1):
        if adjacent(password) and not decreasing(password):
            working += 1
    return working


def part_1(puzzle: PuzzleInput) -> Any:
    start: int
    end: int
    start, end = parse.parse("{:d}-{:d}", puzzle.raw.strip()).fixed
    return count_passwords(start, end)


def double(num: int) -> bool:
    """
    We don't need to worry that a string has more than one group of the same number.
    """
    digits = str(num)
    for i in range(5):
        if digits[i] == digits[i + 1]:
            if digits.count(digits[i]) == 2:
                return True
    return False


def count_passwords_2(start: int, end: int) -> int:
    working = 0
    for password in range(start, end + 1):
        if not decreasing(password) and double(password):
            working += 1
    return working


def part_2(puzzle: PuzzleInput) -> Any:
    start: int
    end: int
    start, end = parse.parse("{:d}-{:d}", puzzle.raw.strip()).fixed
    return count_passwords_2(start, end)
