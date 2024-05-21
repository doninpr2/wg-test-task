from typing import List, Callable
from domain.entities.FiguresConnection import FiguresConnection, FiguresConnectionCreationProps
from domain.usecases.connections_usecase_abstract import ConnectionsUseCaseAbstract
from frameworks.storages.storage_abstract import StorageAbstract

class ConnectionsUseCase(ConnectionsUseCaseAbstract):
    def __init__(self, repository: StorageAbstract[FiguresConnection, FiguresConnectionCreationProps]):
        self.connections: List[str] = []
        self.repository = repository
        self.select_subscribers: List[Callable] = []
        self.create_subscribers: List[Callable] = []

    def select_subscribe(self, observer: Callable):
        self.select_subscribers.append(observer)

    def create_subscribe(self, observer: Callable):
        self.create_subscribers.append(observer)
        
    def get_selected(self) -> List[str]:
        return self.connections

    def select(self, itemId: str) -> List[str]:
        try:
            if itemId not in self.connections:
                self.connections.append(itemId)
            else:
                self.connections.remove(itemId)

            for subscriber in self.select_subscribers:
                try:
                    subscriber(self.connections)
                except Exception as e:
                    print(f"Ошибка при уведомлении подписчика о выделении: {e}")

        except Exception as e:
            print(f"Ошибка выделения элемента: {e}")
        
        return self.connections

    def create(self) -> FiguresConnection:
        try:
            if len(self.connections) < 2:
                raise ValueError("Не достаточно выделений для создания связи")

            connection = self.repository.add(connection=(self.connections[0], self.connections[1]))
            self.connections = []

            for subscriber in self.create_subscribers:
                try:
                    subscriber(connection)
                except Exception as e:
                    print(f"Ошибка при уведомлении подписчика о создании: {e}")

            for subscriber in self.select_subscribers:
                try:
                    subscriber(self.connections)
                except Exception as e:
                    print(f"Ошибка при уведомлении подписчика о выделении: {e}")

            return connection

        except Exception as e:
            print(f"Ошибка при создании связи: {e}")
            return None

    def get_connections(self) -> List[str]:
        return self.connections
