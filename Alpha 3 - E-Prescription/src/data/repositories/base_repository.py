from abc import ABC, abstractmethod
from src.data.db_manager import DatabaseManager


class BaseRepository(ABC):
    """
    Abstract Base Class for a repository.

    This class provides an interface for a repository, which is a class that handles
    all interactions with the database. It uses the DatabaseManager to perform these
    operations.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db: DatabaseManager):
        """
        The constructor for the BaseRepository class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        self.db = db

    @abstractmethod
    def get_all(self):
        """
        Abstract method to get all entities from the database.

        This method should be overridden by any concrete class that inherits from this class.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        """
        Abstract method to get an entity by its ID from the database.

        This method should be overridden by any concrete class that inherits from this class.

        Parameters:
            id (int): The ID of the entity to retrieve.
        """
        pass

    @abstractmethod
    def add(self, entity):
        """
        Abstract method to add an entity to the database.

        This method should be overridden by any concrete class that inherits from this class.

        Parameters:
            entity: The entity to add to the database.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Abstract method to update an entity in the database.

        This method should be overridden by any concrete class that inherits from this class.

        Parameters:
            entity: The entity to update in the database.
        """
        pass

    @abstractmethod
    def delete(self, entity):
        """
        Abstract method to delete an entity from the database.

        This method should be overridden by any concrete class that inherits from this class.

        Parameters:
            entity: The entity to delete from the database.
        """
        pass
