from typing import Protocol, Tuple

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

    def __repr__(self):
        return f"ColoredFigure(id='{self.id}', position={self.position}, color='{self.color}, width={self.width}, height={self.height}')"
