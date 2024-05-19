from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract
from frameworks.storages.storage_abstract import StorageAbstract

class FigureUseCase(FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
    def __init__(self, repository: StorageAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
        self.repository = repository

    def create(self, **kwargs):
        return self.repository.add(**kwargs)

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def move(self, id, pos_x, pos_y):
        rect = self.repository.get(id)
        if rect is None:
            return None
        
        rect.position = (pos_x, pos_y)
        return self.repository.update(rect)