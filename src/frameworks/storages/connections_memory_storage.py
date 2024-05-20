import uuid
from domain.entities.FiguresConnection import FiguresConnection, FiguresConnectionCreationProps
from frameworks.storages.storage_abstract import StorageAbstract

"""Implementation of the storage for connections in memory."""
class ConnectionsMemoryStorage(StorageAbstract[FiguresConnection, FiguresConnectionCreationProps]):
    def __init__(self):
        self.connections = {}

    def add(self, **kwargs: FiguresConnectionCreationProps):
        """Add a connection to the storage."""
        id = str(uuid.uuid4())
        connection = FiguresConnection(id=id, **kwargs)
        self.connections[id] = connection
        return connection

    def get(self, id: str):
        """Get a connection from the storage by its ID."""
        return self.connections.get(id, None)
    
    def get_all(self):
        """Get all connections from the storage."""
        return list(self.connections.values())
    
    def update(self, connection: FiguresConnection):
        """Update connection in the storage."""
        self.connections[connection.id] = connection
        return self.connections[connection.id]
        
    def __repr__(self):
        return f"ConnectionsMemoryStorage(connections={self.connections})"