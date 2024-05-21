import pytest
from domain.entities.colored_rectangle import ColoredRectangle
from domain.utils.collisions_tools import do_rectangles_intersect

def test_colored_rectangle_init():
    rect = ColoredRectangle(id="1", width=100, height=50, position=(10, 20), color="blue")
    
    assert rect.id == "1"
    assert rect.initial_position == (10, 20)
    assert rect.position == (10, 20)
    assert rect.width == 100
    assert rect.height == 50
    assert rect.color == "blue"

def test_get_bbox():
    rect = ColoredRectangle(id="1", width=100, height=50, position=(10, 20), color="blue")
    
    expected_bbox = ((10, 70), (110, 20))
    assert rect.get_bbox() == expected_bbox

def test_is_collided():
    rect1 = ColoredRectangle(id="1", width=100, height=50, position=(10, 20), color="blue")
    rect2 = ColoredRectangle(id="2", width=100, height=50, position=(50, 30), color="red")
    rect3 = ColoredRectangle(id="3", width=100, height=50, position=(200, 300), color="green")
    
    assert rect1.is_collided(rect2) is True
    assert rect1.is_collided(rect3) is False
