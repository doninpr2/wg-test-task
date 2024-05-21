from typing import List
from domain.entities.FiguresConnection import FiguresConnection, FiguresConnectionCreationProps
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from frameworks.storages.storage_abstract import StorageAbstract

""" Класс содержащий бизнес-логику для работы с соединениями фигур

    Attributes:
        connections (List[str]): Список идентификаторов фигур, которые были выбраны для соединения
        repository (StorageAbstract[FiguresConnection, FiguresConnectionCreationProps]): Репозиторий для хранения соединений
        select_subscribers (List[Callable]): Список подписчиков на событие выбора фигуры
        create_subscribers (List[Callable]): Список подписчиков на событие создания соединения

"""
class ConnectionsUseCase(ConnectionsUseCaseAbstract):
    def __init__(self, repository: StorageAbstract[FiguresConnection, FiguresConnectionCreationProps]):
        self.connections: List[str] = []
        self.repository = repository
        self.select_subscribers = []
        self.create_subscribers = []

    def select_subscribe(self, observer):
        self.select_subscribers.append(observer)

    def create_subscribe(self, observer):
        self.create_subscribers.append(observer)
        
    def get_selected(self):
        return self.connections

    def select(self, itemId: str) -> List[str]:
        if itemId not in self.connections:
            self.connections.append(itemId)
        else:
            self.connections.remove(itemId)

        for subscriber in self.select_subscribers:
            subscriber(self.connections)
        
        return self.connections

    def create(self) -> FiguresConnection:
        connection = self.repository.add(connection = (self.connections[0], self.connections[1]))
        self.connections = []

        for subscriber in self.create_subscribers:
          subscriber(connection)
        for subscriber in self.select_subscribers:
          subscriber(self.connections)

        return connection

    def get_connections(self):
        return self.connections