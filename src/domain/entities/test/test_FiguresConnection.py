import pytest
from domain.entities.FiguresConnection import FiguresConnection

def test_figures_connection_init():
    connection = FiguresConnection(id="1", connection=("start_id", "end_id"))
    
    assert connection.id == "1"
    assert connection.connection == ("start_id", "end_id")

if __name__ == "__main__":
    pytest.main()
