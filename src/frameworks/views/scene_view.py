import random

from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract

class SceneView(QGraphicsScene):
    def __init__(self, figure_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], parent=None):
        super().__init__(parent)
        self.figure_usecase = figure_usecase

    def draw_figure(self, figure: ColoredRectangle):
        rect_item = QGraphicsRectItem(figure.position[0], figure.position[1], figure.width, figure.height)
        rect_item.setBrush(figure.color)
        rect_item.setPen(figure.color)
        self.addItem(rect_item)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            rect_width = 100
            rect_height = 50
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pos = event.scenePos()
            position = (pos.x() - (rect_width / 2), pos.y() - (rect_height / 2))

            new_figure = self.figure_usecase.create(position = position, width = rect_width, height = rect_height, color = color)
            self.draw_figure(new_figure)