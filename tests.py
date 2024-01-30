from segment import LineSegment

def main():
    line_one = LineSegment((2, 3), (5, 2))
    line_two = LineSegment((2, 1), (4, 4))
    print(line_one.intersects_with(line_two)) # Expected Value: True
    print(line_two.intersects_with(line_one)) # Expected Value: True
    print(line_one.get_intersection_point_with(line_two))

if __name__ == '__main__':
    main()