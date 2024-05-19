from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PyQt6.QtCore import Qt, QPointF

from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract

class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, figure: ColoredRectangle, use_case: FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
        self.use_case = use_case
        super().__init__(figure.position[0], figure.position[1], figure.width, figure.height)
        self.id = figure.id
        self.setBrush(figure.color)
        self.setPen(figure.color)
        self.prev_pos = self.pos()

        self.setFlags(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable | QGraphicsRectItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)

    def itemChange(self, change: 'QGraphicsItem.GraphicsItemChange', value: QPointF):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            self.prev_pos = self.pos()
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
            if not self.has_collision():
                self.use_case.move(self.id, value.x(), value.y())
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

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.setCursor(Qt.CursorShape.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().mouseReleaseEvent(event)
