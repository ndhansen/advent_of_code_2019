from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Any

from aoc_2019.day_2 import PuzzleInput


class OpCode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LT = 7
    EQ = 8


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

        match opcode:
            case OpCode.OUTPUT:
                modes = [Mode(int(padded[2]))]
            case OpCode.JIT | OpCode.JIF:
                modes = [Mode(int(x)) for x in padded[-3:0:-1]]
            case OpCode.ADD | OpCode.MULTIPLY | OpCode.LT | OpCode.EQ:
                modes = [Mode(int(x)) for x in padded[-3::-1]]
        return Parameter(
            opcode=opcode,
            modes=modes,
        )

    def eval(self, idx: int, numbers: list[int]) -> int:
        # print(self.debug_output(idx, numbers))
        match self.opcode:
            case OpCode.ADD:
                first, second = self.get_inputs(idx, numbers)
                output = first + second
                numbers[numbers[idx + 3]] = output
                return idx + 4
            case OpCode.MULTIPLY:
                first, second = self.get_inputs(idx, numbers)
                output = first * second
                numbers[numbers[idx + 3]] = output
                return idx + 4
            case OpCode.OUTPUT:
                match self.modes[0]:
                    case Mode.IMMEDIATE:
                        output = numbers[idx + 1]
                    case Mode.POSITION:
                        output = numbers[numbers[idx + 1]]
                print("Output:", output)
                return idx + 2
            case OpCode.JIT:
                to_check, out = self.get_inputs(idx, numbers)
                match to_check:
                    case 0:
                        return idx + 3
                    case _:
                        return out
            case OpCode.JIF:
                to_check, out = self.get_inputs(idx, numbers)
                match to_check:
                    case 0:
                        return out
                    case _:
                        return idx + 3
            case OpCode.LT:
                first, second = self.get_inputs(idx, numbers)
                if first < second:
                    numbers[numbers[idx + 3]] = 1
                else:
                    numbers[numbers[idx + 3]] = 0
                return idx + 4
            case OpCode.EQ:
                first, second = self.get_inputs(idx, numbers)
                if first == second:
                    numbers[numbers[idx + 3]] = 1
                else:
                    numbers[numbers[idx + 3]] = 0
                return idx + 4

    def get_inputs(self, idx: int, numbers: list[int]) -> tuple[int, int]:
        match self.modes[0]:
            case Mode.POSITION:
                first = numbers[numbers[idx + 1]]
            case Mode.IMMEDIATE:
                first = numbers[idx + 1]
        match self.modes[1]:
            case Mode.POSITION:
                second = numbers[numbers[idx + 2]]
            case Mode.IMMEDIATE:
                second = numbers[idx + 2]

        return first, second

    def debug_output(self, idx: int, numbers: list[int]) -> str:
        text = "OpCode: " + self.opcode.name
        text += "\n  Modes:"
        for i, mode in enumerate(self.modes, start=1):
            text += f"\n    mode {i}: {mode.name}: "
            match mode:
                case Mode.POSITION:
                    text += f"({numbers[idx+i]}) {numbers[numbers[idx+i]]}"
                case Mode.IMMEDIATE:
                    text += f"{numbers[idx+i]}"
        return text


def run_program(program: list[int], user_input: int) -> Any:
    numbers = program.copy()

    idx = 0

    while True:
        match numbers[idx]:
            case 99:
                break
            case 3:
                numbers[numbers[idx + 1]] = user_input
                idx += 2
            case _:
                parameter = Parameter.parse(numbers[idx])
                idx = parameter.eval(idx, numbers)


def part_1(puzzle: PuzzleInput) -> Any:
    numbers = [int(x) for x in puzzle.raw.replace("\n", "").split(",")]

    run_program(numbers, 1)


def part_2(puzzle: PuzzleInput) -> Any:
    numbers = [int(x) for x in puzzle.raw.replace("\n", "").split(",")]

    print("Part 2:")
    run_program(numbers, 5)
