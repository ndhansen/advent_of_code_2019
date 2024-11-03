import operator
from dataclasses import dataclass
from typing import Any

import parse
from aoc import Coord, Direction

from aoc_2019.utils.contents import PuzzleInput


@dataclass(frozen=True)
class Instruction:
    direction: Direction
    count: int

    def get_vector(self) -> Coord:
        match self.direction:
            case Direction.NORTH:
                return Coord(0, self.count)
            case Direction.SOUTH:
                return Coord(0, -self.count)
            case Direction.EAST:
                return Coord(-self.count, 0)
            case Direction.WEST:
                return Coord(self.count, 0)


def wire_to_instruction(path: str) -> list[Instruction]:
    instructions = []
    for result in parse.findall("{direction:l}{steps:d}", path):
        match result.named["direction"]:
            case "R":
                direction = Direction.EAST
            case "L":
                direction = Direction.WEST
            case "U":
                direction = Direction.NORTH
            case "D":
                direction = Direction.SOUTH
            case _:
                raise ValueError("Unknown direction")

        instructions.append(Instruction(direction, result.named["steps"]))

    return instructions


def get_all_between(first: Coord, second: Coord) -> list[Coord]:
    """
    Gets all coordinates between the first and the second, including the second,
    without the first. Must be straight line.
    """
    if first.col == second.col:
        step = 1 if second.row > first.row else -1
        return [
            Coord(first.col, y)
            for y in range(first.row + step, second.row + step, step)
        ]
    if first.row == second.row:
        step = 1 if second.col > first.col else -1
        return [
            Coord(x, first.row)
            for x in range(first.col + step, second.col + step, step)
        ]
    raise ValueError("Must be on the same x or y axis.")


def generate_coordinates(instructions: list[Instruction]) -> list[Coord]:
    start = Coord(0, 0)
    all_positions = []
    for instruction in instructions:
        coords = get_all_between(start, start + instruction.get_vector())
        all_positions.extend(coords)
        start = coords[-1]
    return all_positions


def part_1(puzzle: PuzzleInput) -> Any:
    wire_1_instructions = wire_to_instruction(puzzle.lines[0])
    wire_2_instructions = wire_to_instruction(puzzle.lines[1])
    wire_1_coords = generate_coordinates(wire_1_instructions)
    wire_2_coords = generate_coordinates(wire_2_instructions)
    overlap = sorted(list(set(wire_1_coords) & set(wire_2_coords)))
    assert len(overlap) > 0
    smallest: Coord = overlap[0]
    return abs(smallest.col) + abs(smallest.row)


def count_steps(path: list[Coord], target: Coord) -> int:
    steps = 0
    for place in path:
        steps += 1
        if place == target:
            return steps
    raise ValueError("No overlap in path.")


def part_2(puzzle: PuzzleInput) -> Any:
    wire_1_instructions = wire_to_instruction(puzzle.lines[0])
    wire_2_instructions = wire_to_instruction(puzzle.lines[1])
    wire_1_coords = generate_coordinates(wire_1_instructions)
    wire_2_coords = generate_coordinates(wire_2_instructions)
    overlap = list(set(wire_1_coords) & set(wire_2_coords))
    wire_1_times = list(map(lambda target: count_steps(wire_1_coords, target), overlap))
    wire_2_times = list(map(lambda target: count_steps(wire_2_coords, target), overlap))
    combined_times = list(
        map(
            lambda time: operator.add(time[0], time[1]), zip(wire_1_times, wire_2_times)
        )
    )
    return min(combined_times)
