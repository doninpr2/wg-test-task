from typing import Protocol, Tuple

class FiguresConnectionCreationProps(Protocol):
    connection: Tuple[str, str]

class FiguresConnectionProps(FiguresConnectionCreationProps):
    id: str

class FiguresConnection:
    def __init__(self, id: str, connection: Tuple[str, str]):
        self.id = id
        self.connection = connection
    
    def __repr__(self):
        return f"FiguresConnection(connection={self.connection})"