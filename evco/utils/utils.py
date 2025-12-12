from __future__ import annotations
from evco.grid.point import Point
from evco.grid.direction import Direction
from typing import Iterable, Type, Generator


def iter_groups(iterable: Iterable, n: int = 2):
    a = [iter(iterable)] * n
    return zip(*a)

def adjacent_points(point: Point, diagonal: bool = False) -> Generator[Point]:
    yield from (point + d.movement for d in Direction)
    if diagonal:
        yield from (point + d for d in [(-1, -1), (-1, 1), (1, -1), (1, 1)])

def adjacent_points_and_dir(point: Point, dir_type: Type[Direction] = Direction) -> Generator[Direction, Point]:
    yield from ((d, point + d.movement) for d in dir_type)
