from enum import Enum
from typing import NamedTuple


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"


class Coord(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Coord") -> "Coord":
        return Coord(x=self.x + other.x, y=self.y + other.y)

    def __lt__(self, other: "Coord") -> bool:
        self_dist = abs(self.x) + abs(self.y)
        other_dist = abs(other.x) + abs(other.y)
        return self_dist < other_dist
