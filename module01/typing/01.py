from typing import Dict, Tuple

# Using Sphinx with autodoc Extension


class Point:
    pass


Point = Tuple[int, int]  # Alias for a tuple representing a point


def get_distance(p1: Point, p2: Point) -> float:
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    return (x_diff**2 + y_diff**2) ** 0.5
