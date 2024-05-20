from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PyQt6.QtCore import Qt, QPointF

from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract

class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, figure: ColoredRectangle, figures_usecase: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps], connections_usecase: ConnectionsUseCaseAbstract):
        self.figures_usecase = figures_usecase
        self.connections_usecase = connections_usecase
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
        self.setZValue(0)

    def itemChange(self, change: 'QGraphicsItem.GraphicsItemChange', value: QPointF):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            self.prev_pos = self.pos()
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            if not self.has_collision():
                positon = self.pos()
                self.figures_usecase.move(self.id, positon.x(), positon.y())
                return super().itemChange(change, value)
            else:
                self.setPos(self.prev_pos)
        else:
          return super().itemChange(change, value)
    
    def has_collision(self):
        # items = self.collidingItems()
        # for item in items:
        #     if isinstance(item, DraggableRectItem) and item.id is not self.id:
        #         return True
        return False
    
    def onSelect(self, connections: list[str]):
        try:
          print(connections.index(self.id))
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
