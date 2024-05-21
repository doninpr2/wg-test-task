import uuid
from domain.entities.figures_connection import FiguresConnection, FiguresConnectionCreationProps
from frameworks.storages.storage_abstract import StorageAbstract

""" Реализация хранилища для соединений фигур """
class ConnectionsMemoryStorage(StorageAbstract[FiguresConnection, FiguresConnectionCreationProps]):
    def __init__(self):
        self.connections = {}

    def add(self, **kwargs: FiguresConnectionCreationProps):
        id = str(uuid.uuid4())
        connection = FiguresConnection(id=id, **kwargs)
        self.connections[id] = connection
        return connection

    def get(self, id: str):
        return self.connections.get(id, None)
    
    def get_all(self):
        return list(self.connections.values())
    
    def update(self, connection: FiguresConnection):
        self.connections[connection.id] = connection
        return self.connections[connection.id]
    
    def delete(self, id: str):
        connection = self.connections.pop(id, None)
        return connection
        
    def __repr__(self):
        return f"ConnectionsMemoryStorage(connections={self.connections})"