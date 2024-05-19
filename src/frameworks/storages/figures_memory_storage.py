import uuid
from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from frameworks.storages.storage_abstract import StorageAbstract

"""Implementation of the storage for figures in memory."""
class FiguresMemoryStorage(StorageAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
    def __init__(self):
        self.figures = {}

    def add(self, **kwargs: ColoredRectangleCreationProps):
        """Add a figure to the storage."""
        figure_id = str(uuid.uuid4())
        figure = ColoredRectangle(id=figure_id, **kwargs)
        self.figures[figure_id] = figure
        return figure

    def get(self, id: str):
        """Get a figure from the storage by its ID."""
        return self.figures.get(id, None)
    
    def get_all(self):
        """Get all figures from the storage."""
        return list(self.figures.values())
    
    def update(self, figure: ColoredRectangle):
        """Update figure in the storage."""
        self.figures[figure.id] = figure
        return self.figures[figure.id]
        
    def __repr__(self):
        return f"FiguresStorage(figures={self.figures})"