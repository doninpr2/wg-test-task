from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, List

T = TypeVar('T')
CreateProps = TypeVar('CreateProps', bound=Any)

class FigureUseCaseAbstract(ABC, Generic[T, CreateProps]):
    @abstractmethod
    def create(self, **kwargs: CreateProps) -> T:
        """ Create a figure. """
        pass

    @abstractmethod
    def get(self, id: str) -> T:
        """ Get a figure by its ID. """
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """ Get all figures. """
        pass

    @abstractmethod
    def move(self, id: str, pos_x: float, pos_y: float) -> T:
        """ Move the figure to the given position. """
        pass