from typing import Protocol, Tuple

from domain.utils.collisions_tools import do_rectangles_intersect

class ColoredRectangleCreationProps(Protocol):
    position: Tuple[float, float]
    width: float
    height: float
    color: str

class ColoredRectangleProps(ColoredRectangleCreationProps):
    id: str

class ColoredRectangle(ColoredRectangleProps):
    def __init__(self, id: str, width: float, height: float, position: tuple = (0, 0), color: str = 'white'):
        self.id = id
        self.initial_position = position
        self.position = position
        self.width = width
        self.height = height
        self.color = color

    def get_bbox(self):
        return (self.position[0], self.position[1] + self.height), (self.position[0] + self.width, self.position[1])

    def is_collided(self, rect: 'ColoredRectangle'):

        rect1_bottom_left, rect1_top_right = self.get_bbox()
        rect2_bottom_left, rect2_top_right = rect.get_bbox()

        return do_rectangles_intersect(rect1_bottom_left, rect1_top_right, rect2_bottom_left, rect2_top_right)

    def __repr__(self):
        return f"ColoredFigure(id='{self.id}', position={self.position}, color='{self.color}, width={self.width}, height={self.height}')"
