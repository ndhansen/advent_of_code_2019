from collections import defaultdict
from typing import Any

from aoc import bfs
from aoc.puzzle import PuzzleInput


def parse_input(
    puzzle: PuzzleInput, bidirectional: bool = False
) -> dict[str, set[str]]:
    orbits = defaultdict(set)
    for raw_orbits in puzzle.lines:
        source, target = raw_orbits.split(")", 1)
        orbits[source].add(target)
        if bidirectional:
            orbits[target].add(source)
    return orbits


def count_orbits(orbits: dict[str, set[str]], current: str, count: int) -> int:
    if current not in orbits:
        return count
    total = count
    for orbit in orbits[current]:
        total += count_orbits(orbits, orbit, count + 1)
    return total


def part_1(puzzle: PuzzleInput) -> Any:
    orbits = parse_input(puzzle)
    return count_orbits(orbits, "COM", 0)


def part_2(puzzle: PuzzleInput) -> Any:
    orbits = parse_input(puzzle, bidirectional=True)
    _, cost = bfs.breadth_first_search(start="YOU", goal="SAN", paths=orbits)
    return cost - 2
