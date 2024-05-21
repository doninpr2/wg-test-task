import pytest
import uuid
from src.domain.entities.figures_connection import FiguresConnection
from frameworks.storages.connections_memory_storage import ConnectionsMemoryStorage

@pytest.fixture
def storage():
    return ConnectionsMemoryStorage()

def test_add_connection(storage):
    connection = storage.add(connection=("1", "2"))
    
    assert isinstance(connection, FiguresConnection)
    assert connection.connection == ("1", "2")
    assert connection.id in storage.connections

def test_get_connection(storage):
    connection = storage.add(connection=("1", "2"))
    retrieved_connection = storage.get(connection.id)
    
    assert retrieved_connection == connection

def test_get_connection_not_found(storage):
    connection_id = str(uuid.uuid4())
    retrieved_connection = storage.get(connection_id)
    
    assert retrieved_connection is None

def test_get_all_connections(storage):
    connection1 = storage.add(connection=("1", "2"))
    connection2 = storage.add(connection=("3", "4"))
    
    all_connections = storage.get_all()
    
    assert len(all_connections) == 2
    assert connection1 in all_connections
    assert connection2 in all_connections

def test_update_connection(storage):
    connection = storage.add(connection=("1", "2"))
    connection.connection = ("5", "6")
    
    updated_connection = storage.update(connection)
    
    assert updated_connection.connection == ("5", "6")
