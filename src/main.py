import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QVBoxLayout, QWidget, QGraphicsScene
from container import Container

class MainWindow(QMainWindow):
    def __init__(self, scene: QGraphicsScene):
      super().__init__()
      self.scene = scene

      self.view = QGraphicsView(self.scene, self)

      central_widget = QWidget()
      layout = QVBoxLayout()
      layout.addWidget(self.view)
      layout.setContentsMargins(0, 0, 0, 0)
      central_widget.setLayout(layout)
      self.setCentralWidget(central_widget)

      self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
      self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

      scene_rect = self.scene.sceneRect().getRect()
      width = scene_rect[2]
      height = scene_rect[3]

      self.setWindowTitle('Double Click to Create Rectangle')
      self.setFixedSize(width, height)
      self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)

      self.view.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
      self.view.resetTransform()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    container = Container()

    scene_view = container.scene_view()
    window = MainWindow(scene_view)
    window.show()

    sys.exit(app.exec())
