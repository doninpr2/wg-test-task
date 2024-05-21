import random

from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

from src.domain.entities.colored_rectangle import ColoredRectangle, ColoredRectangleCreationProps
from src.domain.entities.figures_connection import FiguresConnection
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract
from frameworks.views.connection_view import ConnectionItem
from frameworks.views.rect_view import DraggableRectItem
from constants import rectangle_height, rectangle_width

""" Реализация QGraphicsScene для отображения фигур и соединений

    Attributes:
        figures_usecase (FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]): Используемый usecase для работы с фигурами
        connections_usecase (ConnectionsUseCaseAbstract): Используемый usecase для работы с соединениями
        width (float): Ширина сцены
        height (float): Высота сцены
        parent (Any): Родительский элемент
    
"""
class SceneView(QGraphicsScene):
    def __init__(self, figures_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], connections_usecase: ConnectionsUseCaseAbstract, width: float, height: float, parent=None):
        super().__init__(0, 0, width, height, parent)

        self.connections_usecase = connections_usecase
        self.figures_usecase = figures_usecase

        self.connections_usecase.create_subscribe(self.draw_connection)

        self.setBackgroundBrush(QColor('white'))

    def draw_connection(self, connection: FiguresConnection):
        line_item = ConnectionItem(self.figures_usecase, self.connections_usecase, connection, 'black', 2)
        self.addItem(line_item)

    def draw_figure(self, figure: ColoredRectangle):
        rect_item = DraggableRectItem(figure, self.figures_usecase, connections_usecase=self.connections_usecase, scene=self)
        self.addItem(rect_item)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            rect_width = rectangle_width
            rect_height = rectangle_height
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pos = event.scenePos()
            position = (pos.x() - (rect_width / 2), pos.y() - (rect_height / 2))

            if self.sceneRect().contains(position[0], position[1]) and self.sceneRect().contains(position[0] + rect_width, position[1] + rect_height):
                new_figure = self.figures_usecase.create(position = position, width = rect_width, height = rect_height, color = color)
                if new_figure is not None:
                    self.draw_figure(new_figure)
            