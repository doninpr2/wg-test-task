import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QVBoxLayout, QWidget
from container import Container

class ResizableGraphicsView(QGraphicsView):
    def resizeEvent(self, event):
        self.fitInView(self.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        super().resizeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self, scene):
      super().__init__()

      # Create a QGraphicsScene
      self.scene = scene

      # Create a QGraphicsView to visualize the scene
      self.view = QGraphicsView(self.scene, self)

      # Make the QGraphicsView fill the entire window
      central_widget = QWidget()
      layout = QVBoxLayout()
      layout.addWidget(self.view)
      central_widget.setLayout(layout)
      self.setCentralWidget(central_widget)

      # Set the scene rect to match the size of the view
      self.view.setSceneRect(0, 0, self.width(), self.height())
      self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
      self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

      # Connect the resize event to adjust the scene rect
      self.view.resizeEvent = self.on_resize

      # Set window dimensions
      self.setGeometry(100, 100, 800, 600)
      self.setWindowTitle('Double Click to Create Rectangle')

    def on_resize(self, event):
        self.view.setSceneRect(0, 0, self.view.width(), self.view.height())
        QGraphicsView.resizeEvent(self.view, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create the dependency injection container
    container = Container()

    # Get an instance of SceneView from the container
    scene_view = container.scene_view()

    # Create and show the main window
    window = MainWindow(scene_view)
    window.show()

    sys.exit(app.exec())
