
def do_rectangles_intersect(rect1_bottom_left: tuple[float, float], rect1_top_right: tuple[float, float], rect2_bottom_left: tuple[float, float], rect2_top_right: tuple[float, float]):
    """Check if two rectangles intersect.
    
    Args:
        rect1_bottom_left: Tuple (x1, y1) for the bottom-left corner of the first rectangle.
        rect1_top_right: Tuple (x2, y2) for the top-right corner of the first rectangle.
        rect2_bottom_left: Tuple (x3, y3) for the bottom-left corner of the second rectangle.
        rect2_top_right: Tuple (x4, y4) for the top-right corner of the second rectangle.
        
    Returns:
        True if the rectangles intersect, False otherwise.
    """

    x1, y1 = rect1_bottom_left
    x2, y2 = rect1_top_right
    x3, y3 = rect2_bottom_left
    x4, y4 = rect2_top_right

    if ((x1 <= x3 and x3 <= x2) or (x1 <= x4 and x4 <= x2)) and ((y2 <= y3 and y3 <= y1) or (y2 <= y4 and y4 <= y1)):
        return True

    return False

def is_point_inside_rect(point: tuple[float, float], rect_bottom_left: tuple[float, float], rect_top_right: tuple[float, float]):
    """Check if a point is inside a rectangle.
    
    Args:
        point: Tuple (x, y) for the point.
        rect_bottom_left: Tuple (x1, y1) for the bottom-left corner of the rectangle.
        rect_top_right: Tuple (x2, y2) for the top-right corner of the rectangle.
        
    Returns:
        True if the point is inside the rectangle, False otherwise.
    """

    x, y = point
    x1, y1 = rect_bottom_left
    x2, y2 = rect_top_right

    if x1 <= x and x <= x2 and y1 <= y and y <= y2:
        return True

    return False
