import pytest
from domain.utils.collisions_tools import do_rectangles_intersect, is_point_inside_rect

def test_do_rectangles_intersect_intersecting():
    rect1_bottom_left = (1, 3)
    rect1_top_right = (3, 1)
    rect2_bottom_left = (2, 4)
    rect2_top_right = (4, 2)
    assert do_rectangles_intersect(rect1_bottom_left, rect1_top_right, rect2_bottom_left, rect2_top_right) is True

def test_do_rectangles_intersect_non_intersecting():
    rect1_bottom_left = (1, 3)
    rect1_top_right = (3, 1)
    rect2_bottom_left = (4, 6)
    rect2_top_right = (6, 4)
    assert do_rectangles_intersect(rect1_bottom_left, rect1_top_right, rect2_bottom_left, rect2_top_right) is False

def test_is_point_inside_rect_inside():
    point = (1, 1)
    rect_bottom_left = (0, 0)
    rect_top_right = (2, 2)
    assert is_point_inside_rect(point, rect_bottom_left, rect_top_right) is True

def test_is_point_inside_rect_outside():
    point = (3, 3)
    rect_bottom_left = (0, 0)
    rect_top_right = (2, 2)
    assert is_point_inside_rect(point, rect_bottom_left, rect_top_right) is False

def test_is_point_inside_rect_on_edge():
    point = (2, 2)
    rect_bottom_left = (0, 0)
    rect_top_right = (2, 2)
    assert is_point_inside_rect(point, rect_bottom_left, rect_top_right) is True

def test_is_point_inside_rect_on_corner():
    point = (0, 0)
    rect_bottom_left = (0, 0)
    rect_top_right = (2, 2)
    assert is_point_inside_rect(point, rect_bottom_left, rect_top_right) is True

if __name__ == "__main__":
    pytest.main()
