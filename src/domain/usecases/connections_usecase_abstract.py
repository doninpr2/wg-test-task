
from abc import ABC, abstractmethod
from typing import List

from domain.entities.figures_connection import FiguresConnection

class ConnectionsUseCaseAbstract(ABC):

    @abstractmethod
    def select_subscribe(self, observer):
        """ Subscribe to select event. """
        pass

    @abstractmethod
    def create_subscribe(self, observer):
        """ Subscribe to create event. """
        pass

    @abstractmethod
    def select(self, itemId: str) -> List[str]:
        """ Select item. """
        pass

    @abstractmethod
    def get_connections(self) -> List[FiguresConnection]:
        """ Get all connections. """
        pass

    @abstractmethod
    def create(self) -> FiguresConnection:
        """ Create connection. """
        pass

    @abstractmethod
    def get_selected(self) -> List[str]:
        """ Get selected connections. """
        pass

    @abstractmethod
    def delete(self, itemId: str):
        """ Delete connection. """
        pass