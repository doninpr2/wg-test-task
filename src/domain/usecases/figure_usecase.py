from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract
from frameworks.storages.storage_abstract import StorageAbstract

class FigureUseCase(FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
    def __init__(self, repository: StorageAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
        self.repository = repository
        self.move_subscribers = []

    def move_subcribe(self, observer):
        self.move_subscribers.append(observer)

    def create(self, **kwargs):
        print('create', kwargs)
        return self.repository.add(**kwargs)

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def move(self, id, pos_x, pos_y):
        rect = self.repository.get(id)
        if rect is None:
            return None
        
        rect.position = (rect.initial_position[0] + pos_x, rect.initial_position[1] + pos_y)

        for subscriber in self.move_subscribers:
            subscriber(rect)

        return self.repository.update(rect)