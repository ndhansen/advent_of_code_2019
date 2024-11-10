from collections import defaultdict, deque
from typing import Any

from aoc_2019.utils.contents import PuzzleInput


def parse_input(
    puzzle: PuzzleInput, bidirectional: bool = False
) -> dict[str, list[str]]:
    orbits = defaultdict(list)
    for raw_orbits in puzzle.lines:
        source, target = raw_orbits.split(")", 1)
        orbits[source].append(target)
        if bidirectional:
            orbits[target].append(source)
    return orbits


def count_orbits(orbits: dict[str, list[str]], current: str, count: int) -> int:
    if current not in orbits:
        return count
    total = count
    for orbit in orbits[current]:
        total += count_orbits(orbits, orbit, count + 1)
    return total


def part_1(puzzle: PuzzleInput) -> Any:
    orbits = parse_input(puzzle)
    return count_orbits(orbits, "COM", 0)


def bfs(orbits: dict[str, list[str]], start: str, end: str) -> int:
    seen = set()
    nodes = deque([(start, 0)])
    while nodes:
        current, dist = nodes.popleft()
        if current in seen:
            continue
        if current == end:
            return dist
        seen.add(current)
        for neighbor in orbits[current]:
            nodes.append((neighbor, dist + 1))
    raise ValueError


def part_2(puzzle: PuzzleInput) -> Any:
    orbits = parse_input(puzzle, bidirectional=True)
    return bfs(orbits, "YOU", "SAN") - 2
