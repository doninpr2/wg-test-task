from PyQt6.QtWidgets import QGraphicsLineItem
from PyQt6.QtGui import QColor, QPen
from PyQt6.QtCore import Qt, QPointF

from domain.entities.colored_rectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.entities.figures_connection import FiguresConnection
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract


""" Реализация QGraphicsLineItem линии для отображения соединения фигур

    Attributes:
        figures_usecase (FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]): Используемый usecase для работы с фигурами
        connections_usecase (ConnectionsUseCaseAbstract): Используемый usecase для работы с соединениями
        connection (FiguresConnection): Соединение фигур
        color (str): Цвет линии
        width (int): Толщина линии
        parent (Any): Родительский элемент

"""
class ConnectionItem(QGraphicsLineItem):
    def __init__(self, figures_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], connections_usecase: ConnectionsUseCaseAbstract, connection: FiguresConnection, color: str = 'black', width: int = 2, parent=None):
        self.figures_usecase = figures_usecase
        self.connections_usecase = connections_usecase
        self.connection = connection

        line_points = self.getPositionByFigures()
        start_pos = line_points['start']
        end_pos = line_points['end']
        self.parent = parent

        super().__init__(start_pos[0], start_pos[1], end_pos[0], end_pos[1])

        self.setPen(QPen(QColor(color), width))
        self.setZValue(11)

        self.figures_usecase.move_subcribe(self.onMove)

    # Обновление позиции линии при перемещении фигур
    def onMove(self, figure: ColoredRectangle):
        if figure.id in self.connection.connection:
            line_points = self.getPositionByFigures()
            start_pos = line_points['start']
            end_pos = line_points['end']
            self.setLine(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
        
    # Получение координат для соединения фигур
    def getPositionByFigures(self):
        start_figure = self.figures_usecase.get(self.connection.connection[0])
        end_figure = self.figures_usecase.get(self.connection.connection[1])

        start_pos = (start_figure.position[0] + start_figure.width / 2, start_figure.position[1] + start_figure.height / 2)
        end_pos = (end_figure.position[0] + end_figure.width / 2, end_figure.position[1] + end_figure.height / 2)

        return { 'start': start_pos, 'end': end_pos}
    
    def delete_connection(self):
        try:
            self.connections_usecase.delete(self.connection.id)
            scene = self.scene()
            if scene:
                scene.removeItem(self)
            print(f"Соединение {self.connection.id} удалено")
        except Exception as e:
            print(f"Ошибка при удалении соединения: {e}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.delete_connection()
        super().mousePressEvent(event)