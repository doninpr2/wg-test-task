import pytest
import uuid
from domain.entities.ColoredRectangle import ColoredRectangle, ColoredRectangleCreationProps
from frameworks.storages.figures_memory_storage import FiguresMemoryStorage

@pytest.fixture
def storage():
    return FiguresMemoryStorage()

def test_add_figure(storage):
    figure = storage.add(position=(10, 10), width=100, height=50, color="blue")
    
    assert isinstance(figure, ColoredRectangle)
    assert figure.position == (10, 10)
    assert figure.width == 100
    assert figure.height == 50
    assert figure.color == "blue"
    assert figure.id in storage.figures

def test_get_figure(storage):
    figure = storage.add(position=(10, 10), width=100, height=50, color="blue")
    retrieved_figure = storage.get(figure.id)
    
    assert retrieved_figure == figure

def test_get_figure_not_found(storage):
    figure_id = str(uuid.uuid4())
    retrieved_figure = storage.get(figure_id)
    
    assert retrieved_figure is None

def test_get_all_figures(storage):
    figure1 = storage.add(position=(10, 10), width=100, height=50, color="blue")
    figure2 = storage.add(position=(20, 20), width=200, height=100, color="red")
    
    all_figures = storage.get_all()
    
    assert len(all_figures) == 2
    assert figure1 in all_figures
    assert figure2 in all_figures

def test_update_figure(storage):
    figure = storage.add(position=(10, 10), width=100, height=50, color="blue")
    figure.position = (20, 20)
    figure.width = 200
    figure.height = 100
    figure.color = "red"
    
    updated_figure = storage.update(figure)
    
    assert updated_figure.position == (20, 20)
    assert updated_figure.width == 200
    assert updated_figure.height == 100
    assert updated_figure.color == "red"
