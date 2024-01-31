"""
Line Segment Class.

Sources/Links:
Help with math: https://www.cuemath.com/geometry/intersection-of-two-lines/
"""

from __future__ import annotations
from math import sqrt
from dataclasses import dataclass

__all__ = [
    'Point',
    'LineSegment'
]

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __getitem__(self, idx: int) -> int:
        if idx == 0:
            return self.x
        if idx == 1:
            return self.y
        return None

class LineSegment:

    def __init__(self, point_one: Point | tuple, point_two: Point | tuple) -> None:
        self.point_one = Point(point_one[0], point_one[1])
        self.point_two = Point(point_two[0], point_two[1])

    def length(self) -> float:
        """
        Returns the distance between the two points of the segment.
        Uses the Euclidean Distance Formula.
        """
        return sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
    
    def intersects_with(self, other: LineSegment) -> bool:
        """
        Determines if this line segment is intersecting with the passed segment.
        """

        # Define a helper function for determining the direction of all four points
        def direction(p: Point, q: Point, r: Point) -> float:
            """
            Computes the direction of the three given points.

            Returns a positive value if they perform a counter clockwise orientation.
            Returns a negative value if they form a clockwise orientation.
            Returns zero if they are colinear.
            """
            return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

        # Compute the directions of the four points of the two line segments
        d1 = direction(self.point_one, self.point_two, other.point_one)
        d2 = direction(self.point_one, self.point_two, other.point_two)
        d3 = direction(other.point_one, other.point_two, self.point_one)
        d4 = direction(other.point_one, other.point_two, self.point_two)

        # Check if there is any intersection
        return (
            ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and
            ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0))
        )

    def get_intersection_point_with(self, other: LineSegment, decimal_places: int = -1) -> Point | None:
        """
        Determines where this segment and the passed segment are intersecting. This function
        assumes that there is a valid intersection point.

        The user can specify how many decimal points they want to round the resulting point to. If
        -1 is passed, then no formatting is done.
        """
        # Check if they intersect, user may misuse this function.
        if not self.intersects_with(other):
            return None
        # Get the difference between the line segments coordinates, x and y
        diffx = Point(self.point_one.x - self.point_two.x, other.point_one.x - other.point_two.x)
        diffy = Point(self.point_one.y - self.point_two.y, other.point_one.y - other.point_two.y)

        # Define a simple helper function to calculate the determinant
        def determinant(diffa: Point, diffb: Point) -> int:
            return diffa.x * diffb.y - diffa.y * diffb.x

        # Calculate the divisor
        divisor = determinant(diffx, diffy)

        # Calculate main determinant, and determinants of x and y
        d = Point(determinant(self.point_one, self.point_two), determinant(other.point_one, other.point_two))
        x = determinant(d, diffx) / divisor
        y = determinant(d, diffy) / divisor

        # Check if any custom formatting is requested
        if decimal_places > 0:
            x = round(x, decimal_places)
            y = round(y, decimal_places)

        # Return the intersection
        return Point(x, y)

    def __len__(self) -> float:
        return self.length()
    
    def __repr__(self) -> str:
        return f"{self.point_one} {self.point_two}"
    
    def __str__(self) -> str:
        return self.__repr__()
