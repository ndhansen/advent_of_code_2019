from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Any

import pudb

from aoc_2019.day_2 import PuzzleInput


class OpCode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    OUTPUT = 4


class Mode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1


@dataclass
class Parameter:
    opcode: OpCode
    modes: list[Mode]

    @staticmethod
    def parse(number: int) -> Parameter:
        padded = str(number).rjust(5, "0")
        opcode = OpCode(int(padded[-2:]))

        modes = [Mode(int(x)) for x in padded[-3::-1]]
        in_order_modes = list(reversed(modes))
        return Parameter(
            opcode=opcode,
            modes=in_order_modes,
        )

    def show(self, numbers: list[int]) -> None:
        match self.opcode:
            ...

def get_inputs(parameter: Parameter, idx: int, numbers: list[int]) -> tuple[int, int]:
    match parameter.modes[0]:
        case Mode.POSITION:
            first = numbers[numbers[idx + 1]]
        case Mode.IMMEDIATE:
            first = numbers[idx + 1]
    match parameter.modes[1]:
        case Mode.POSITION:
            second = numbers[numbers[idx + 2]]
        case Mode.IMMEDIATE:
            second = numbers[idx + 2]

    return first, second


def eval_parameter(parameter: Parameter, idx: int, numbers: list[int]) -> int:
    match parameter.opcode:
        case OpCode.ADD:
            first, second = get_inputs(parameter, idx, numbers)
            numbers[numbers[idx + 3]] = first + second
            return 4
        case OpCode.MULTIPLY:
            first, second = get_inputs(parameter, idx, numbers)
            numbers[numbers[idx + 3]] = first * second
            return 4
        case OpCode.OUTPUT:
            match parameter.modes[2]:
                case Mode.IMMEDIATE:
                    output = numbers[idx + 1]
                case Mode.POSITION:
                    output = numbers[numbers[idx + 1]]
            if output != 0:
                import pudb

                pudb.set_trace()
            print(output)
            return 2


def run_program(program: list[int]) -> Any:
    numbers = program.copy()

    idx = 0

    while True:
        match numbers[idx]:
            case 99:
                break
            case 3:
                numbers[numbers[idx + 1]] = 1
                idx += 2
            case _:
                print("debug:", numbers[idx])
                parameter = Parameter.parse(numbers[idx])
                moves = eval_parameter(parameter, idx, numbers)
                idx += moves


def part_1(puzzle: PuzzleInput) -> Any:
    numbers = [int(x) for x in puzzle.raw.split(",")]

    pudb.set_trace()

    run_program(numbers)


def part_2(puzzle: PuzzleInput) -> Any: ...
