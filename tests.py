import unittest
from segment import LineSegment, Point
from plane import Plane

class TestSegmentIntersections(unittest.TestCase):
    
    def test_intersection(self) -> None:
        """
        Test cases where we expect to get an intersection between the two line segments.
        """
        self.assertTrue(LineSegment(Point(2, 3), Point(5, 2)).intersects_with(LineSegment(Point(2, 1), Point(4, 4))))

    def test_no_intersection(self) -> None:
        """
        Test cases where we expect to NOT get an intersection between the two line segments.
        """
        self.assertFalse(LineSegment(Point(1, 1), Point(5, 1)).intersects_with(LineSegment(Point(1, 2), Point(5, 2))))

    def test_invalid_input(self) -> None:
        """
        Tests where the type passed to this function is not valid, i.e not a LineSegment.
        """
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(None)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(int)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(float)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(str)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(Point)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(LineSegment)
        with self.assertRaises(TypeError):
            LineSegment(Point(1, 1), Point(5, 1)).intersects_with(LineSegment())

if __name__ == '__main__':
    unittest.main()