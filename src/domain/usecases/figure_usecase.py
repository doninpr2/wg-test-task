from typing import List, Callable
from domain.entities.colored_rectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase_abstract import FigureUseCaseAbstract
from frameworks.storages.storage_abstract import StorageAbstract
from constants import window_width, window_height

class FigureUseCase(FigureUseCaseAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
    def __init__(self, repository: StorageAbstract[ColoredRectangle, ColoredRectangleCreationProps]):
        self.repository = repository
        self.move_subscribers: List[Callable] = []

    # метод для подписки на событие перемещения фигуры
    def move_subcribe(self, observer: Callable):
        self.move_subscribers.append(observer)

    def create(self, **kwargs) -> ColoredRectangle:
        try:
            temp_rect = ColoredRectangle(id='temp', **kwargs)

            if not self.is_collided(temp_rect):
                return self.repository.add(**kwargs)

            return None
        except Exception as e:
            print(f"Ошибка при создании фигуры: {e}")
            return None

    def get(self, id: str) -> ColoredRectangle:
        try:
            return self.repository.get(id)
        except Exception as e:
            print(f"Ошибка при получении фигуры с id {id}: {e}")
            return None

    def get_all(self) -> List[ColoredRectangle]:
        try:
            return self.repository.get_all()
        except Exception as e:
            print(f"Ошибка при получении всех фигур: {e}")
            return []

    # метод для проверки на пересечение фигур
    def is_collided(self, figure: ColoredRectangle) -> bool:
        try:
            for f in self.get_all():
                if f.id != figure.id and f.is_collided(figure):
                    return True
            return False
        except Exception as e:
            print(f"Ошибка при проверке пересечения фигур: {e}")
            return False

    # метод для перемещения фигуры
    def move(self, id: str, pos_x: float, pos_y: float) -> ColoredRectangle:
        try:
            rect = self.repository.get(id)
            if rect is None:
                return None
            
            rect.position = (rect.initial_position[0] + pos_x, rect.initial_position[1] + pos_y)

            for subscriber in self.move_subscribers:
                try:
                    subscriber(rect)
                except Exception as e:
                    print(f"Ошибка при уведомлении подписчика о перемещении: {e}")

            return self.repository.update(rect)
        except Exception as e:
            print(f"Ошибка при перемещении фигуры с id {id}: {e}")
            return None
