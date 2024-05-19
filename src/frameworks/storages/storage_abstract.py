from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, List

T = TypeVar('T')
CreateProps = TypeVar('CreateProps', bound=Any)

class StorageAbstract(ABC, Generic[T, CreateProps]):
    @abstractmethod
    def add(self, **kwargs: CreateProps) -> T:
        """Add a object to the storage."""
        pass

    @abstractmethod
    def get(self, id: str) -> T:
        """Get a object from the storage by its ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all objects from the storage."""
        pass

    @abstractmethod
    def update(self, object: T) -> T:
        """Update object in the storage."""
        pass
