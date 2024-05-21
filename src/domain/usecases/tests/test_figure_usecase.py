import pytest
from unittest.mock import Mock
from domain.entities.colored_rectangle import ColoredRectangle, ColoredRectangleCreationProps
from domain.usecases.figure_usecase import FigureUseCase
from frameworks.storages.storage_abstract import StorageAbstract

@pytest.fixture
def mock_storage():
    return Mock(spec=StorageAbstract)

@pytest.fixture
def figure_use_case(mock_storage):
    return FigureUseCase(repository=mock_storage)

def test_create_figure_success(figure_use_case, mock_storage):
    mock_storage.add.return_value = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )

    mock_storage.get_all.return_value = []

    new_figure = figure_use_case.create(
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )

    assert new_figure is not None
    assert new_figure.position == (10, 10)
    assert new_figure.width == 100
    assert new_figure.height == 50
    assert new_figure.color == "blue"
    mock_storage.add.assert_called_once_with(
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )

def test_create_figure_collision(figure_use_case, mock_storage):
    existing_figure = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )
    mock_storage.get_all.return_value = [existing_figure]

    new_figure = figure_use_case.create(
        position=(10, 10), 
        width=100, 
        height=50, 
        color="red"
    )

    assert new_figure is None
    mock_storage.add.assert_not_called()

def test_get_figure(figure_use_case, mock_storage):
    figure = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )
    mock_storage.get.return_value = figure

    result = figure_use_case.get("1")

    assert result == figure
    mock_storage.get.assert_called_once_with("1")

def test_move_figure(figure_use_case, mock_storage):
    figure = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )
    mock_storage.get.return_value = figure
    mock_storage.update.return_value = figure

    updated_figure = figure_use_case.move("1", 20, 30)

    assert updated_figure.position == (30, 40)
    mock_storage.update.assert_called_once()
    mock_storage.get.assert_called_once_with("1")

def test_is_collided(figure_use_case, mock_storage):
    existing_figure = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )
    new_figure = ColoredRectangle(
        id="2", 
        position=(15, 15), 
        width=100, 
        height=50, 
        color="red"
    )
    mock_storage.get_all.return_value = [existing_figure]

    result = figure_use_case.is_collided(new_figure)

    assert result is True

def test_no_collision(figure_use_case, mock_storage):
    existing_figure = ColoredRectangle(
        id="1", 
        position=(10, 10), 
        width=100, 
        height=50, 
        color="blue"
    )
    new_figure = ColoredRectangle(
        id="2", 
        position=(200, 200), 
        width=100, 
        height=50, 
        color="red"
    )
    mock_storage.get_all.return_value = [existing_figure]

    result = figure_use_case.is_collided(new_figure)

    assert result is False
