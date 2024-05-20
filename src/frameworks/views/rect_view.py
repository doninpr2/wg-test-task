from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsItem, QGraphicsScene
from PyQt6.QtCore import Qt, QPointF

from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract

class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, figure: ColoredRectangle, figures_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], connections_usecase: ConnectionsUseCaseAbstract, scene: QGraphicsScene):
        self.figures_usecase = figures_usecase
        self.connections_usecase = connections_usecase
        self.parent_scene = scene
        super().__init__(figure.position[0], figure.position[1], figure.width, figure.height)
        self.id = figure.id
        self.color = figure.color
        self.setBrush(figure.color)
        self.setPen(figure.color)
        self.prev_pos = self.pos()

        self.connections_usecase.select_subscribe(self.onSelect)

        self.setFlags(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable | QGraphicsRectItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        self.setZValue(10)

    def itemChange(self, change: 'QGraphicsItem.GraphicsItemChange', value: QPointF):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            self.prev_pos = self.pos()
            if not self.has_collision(value) and self.is_in_scene(value):
                return super().itemChange(change, value)
            else:
                return super().itemChange(change, self.pos())         
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            self.figures_usecase.move(self.id, value.x(), value.y())
            return super().itemChange(change, value)
        else:
          return super().itemChange(change, value)
    
    def has_collision(self, value: QPointF):
        rect = self.figures_usecase.get(self.id)
        if rect is None:
            return False
        
        rect.position = (rect.initial_position[0] + value.x(), rect.initial_position[1] + value.y())
        return self.figures_usecase.is_collided(rect)
    
    def is_in_scene(self, value: QPointF):
        rect = self.figures_usecase.get(self.id)
        if rect is None:
            return False
        
        rect.position = (rect.initial_position[0] + value.x(), rect.initial_position[1] + value.y())
        bottom_left, top_right = rect.get_bbox()
        return self.parent_scene.sceneRect().contains(bottom_left[0], bottom_left[1]) and self.parent_scene.sceneRect().contains(top_right[0], top_right[1])
    
    def onSelect(self, connections: list[str]):
        try:
          if connections.index(self.id) >= 0:
            self.setPen(Qt.GlobalColor.green)
        except ValueError:
            self.setPen(self.color)
    
    def selectItem(self):
        connections = self.connections_usecase.select(self.id)
        if len(connections) == 2:
            self.connections_usecase.create()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
          self.clicked = True
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.clicked:
            self.clicked = False
        super().mouseMoveEvent(event)
        self.setCursor(Qt.CursorShape.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        if self.clicked:
            self.selectItem()
            self.clicked = False
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)
