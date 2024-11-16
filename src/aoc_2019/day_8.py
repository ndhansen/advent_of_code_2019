from typing import Any

from aoc.datatypes import Coord, itertools

from aoc_2019.utils.contents import PuzzleInput


def get_layers(puzzle: PuzzleInput) -> list[list[str]]:
    dimensions = Coord(row=2, col=3) if puzzle.test else Coord(row=6, col=25)
    layers = []
    data = puzzle.raw.strip()
    row = 0
    current_layer = []
    for chunk in range(0, len(data), dimensions.col):
        if row == dimensions.row:
            layers.append(current_layer)
            current_layer = []
            row = 0
        current_layer.append(data[chunk : chunk + dimensions.col])
        row += 1
    layers.append(current_layer)
    return layers


def part_1(puzzle: PuzzleInput) -> Any:
    layers = get_layers(puzzle)

    zero_map = {}
    for index, layer in enumerate(layers):
        zeroes = sum(x.count("0") for x in layer)
        zero_map[index] = zeroes

    smallest_layer = None
    smallest_value = float("inf")
    for index, value in zero_map.items():
        if value < smallest_value:
            smallest_layer = index
            smallest_value = value

    if not smallest_layer:
        raise ValueError

    ones = sum(x.count("1") for x in layers[smallest_layer])
    twos = sum(x.count("2") for x in layers[smallest_layer])
    return ones * twos


def part_2(puzzle: PuzzleInput) -> Any:
    layers = get_layers(puzzle)
    pixels = []
    for row, col in itertools.product(range(len(layers[0])), range(len(layers[0][0]))):
        pixel = Coord(row, col)
        for i in range(len(layers)):
            match layers[i][pixel.row][pixel.col]:
                case "2":
                    continue
                case "1":
                    pixels.append("X")
                    break
                case "0":
                    pixels.append("_")
                    break

    i = 0
    for row in range(len(layers[0])):
        for col in range(len(layers[0][0])):
            print(pixels[i], end="")
            i += 1
        print()
