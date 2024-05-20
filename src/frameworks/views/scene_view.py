import random

from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPen

from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.entities.FiguresConnection import FiguresConnection
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract
from frameworks.views.connection_view import ConnectionItem
from frameworks.views.rect_view import DraggableRectItem

class SceneView(QGraphicsScene):
    def __init__(self, figures_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], connections_usecase: ConnectionsUseCaseAbstract, parent=None):
        super().__init__(parent)
        self.connections_usecase = connections_usecase
        self.figures_usecase = figures_usecase

        self.connections_usecase.create_subscribe(self.draw_connection)

    def draw_connection(self, connection: FiguresConnection):
        line_item = ConnectionItem(self.figures_usecase, self.connections_usecase, connection, 'white', 2)
        self.addItem(line_item)

    def draw_figure(self, figure: ColoredRectangle):
        rect_item = DraggableRectItem(figure, self.figures_usecase, connections_usecase=self.connections_usecase)
        self.addItem(rect_item)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            rect_width = 100
            rect_height = 50
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pos = event.scenePos()
            position = (pos.x() - (rect_width / 2), pos.y() - (rect_height / 2))

            new_figure = self.figures_usecase.create(position = position, width = rect_width, height = rect_height, color = color)
            self.draw_figure(new_figure)