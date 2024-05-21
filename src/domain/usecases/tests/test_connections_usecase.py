import pytest
from unittest.mock import Mock
from domain.entities.figures_connection import FiguresConnection
from domain.usecases.connections_usecase import ConnectionsUseCase
from frameworks.storages.storage_abstract import StorageAbstract

@pytest.fixture
def mock_storage():
    return Mock(spec=StorageAbstract)

@pytest.fixture
def connections_use_case(mock_storage):
    return ConnectionsUseCase(repository=mock_storage)

def test_select_subscribe(connections_use_case):
    observer = Mock()
    connections_use_case.select_subscribe(observer)
    
    connections_use_case.select("item1")
    
    observer.assert_called_once_with(["item1"])

def test_create_subscribe(connections_use_case, mock_storage):
    observer = Mock()
    connections_use_case.create_subscribe(observer)
    
    connection = FiguresConnection(id="1", connection=("item1", "item2"))
    mock_storage.add.return_value = connection
    
    connections_use_case.connections = ["item1", "item2"]
    created_connection = connections_use_case.create()
    
    observer.assert_called_once_with(connection)
    assert created_connection == connection

def test_get_selected(connections_use_case):
    connections_use_case.connections = ["item1", "item2"]
    
    selected = connections_use_case.get_selected()
    
    assert selected == ["item1", "item2"]

def test_select(connections_use_case):
    connections_use_case.select("item1")
    
    assert connections_use_case.get_selected() == ["item1"]
    
    connections_use_case.select("item1")
    
    assert connections_use_case.get_selected() == []

def test_create(connections_use_case, mock_storage):
    connection = FiguresConnection(id="1", connection=("item1", "item2"))
    mock_storage.add.return_value = connection
    
    connections_use_case.connections = ["item1", "item2"]
    created_connection = connections_use_case.create()
    
    assert created_connection == connection
    assert connections_use_case.get_selected() == []
    mock_storage.add.assert_called_once_with(connection=("item1", "item2"))

def test_get_connections(connections_use_case):
    connections_use_case.connections = ["item1", "item2"]
    
    connections = connections_use_case.get_connections()
    
    assert connections == ["item1", "item2"]

def test_delete(connections_use_case, mock_storage):
    connection = FiguresConnection(id="1", connection=("item1", "item2"))
    mock_storage.delete.return_value = connection
    
    deleted_connection = connections_use_case.delete("1")
    
    assert deleted_connection == connection
    mock_storage.delete.assert_called_once_with(id="1")