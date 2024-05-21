import uuid
from domain.entities.colored_rectangle import ColoredRectangle, ColoredRectangleCreationProps
from frameworks.storages.storage_abstract import StorageAbstract

""" Реализация хранилища для фигур """
class FiguresMemoryStorage(StorageAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
    def __init__(self):
        self.figures = {}

    def add(self, **kwargs: ColoredRectangleCreationProps):
        figure_id = str(uuid.uuid4())
        figure = ColoredRectangle(id=figure_id, **kwargs)
        self.figures[figure_id] = figure
        return figure

    def get(self, id: str):
        return self.figures.get(id, None)
    
    def get_all(self):
        return list(self.figures.values())
    
    def update(self, figure: ColoredRectangle):
        self.figures[figure.id] = figure
        return self.figures[figure.id]
    
    def delete(self, id: str):
        figure = self.figures.pop(id, None)
        return figure
        
    def __repr__(self):
        return f"FiguresStorage(figures={self.figures})"