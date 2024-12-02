from typing import override

from src.data.models.specialization import Specialization
from src.data.repositories.base_repository import BaseRepository

class SpecializationRepo(BaseRepository):
    """
    A repository for managing Specialization entities in the database.

    Inherits from:
        BaseRepository: A base class for all repositories.
    """

    def __init__(self, db):
        """
        Initialize a new instance of the SpecializationRepo class.

        Args:
            db: A database connection object.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Retrieve all Specialization entities from the database.

        Returns:
            A list of Specialization entities.
        """
        query = "SELECT * FROM specialization"
        result = self.db.fetch(query)
        return [Specialization(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Retrieve a Specialization entity by its ID.

        Args:
            id (int): The ID of the Specialization entity.

        Returns:
            A Specialization entity if found, None otherwise.
        """
        query = "SELECT * FROM specialization WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Specialization(*result)

    @override
    def add(self, specialization: Specialization):
        """
        Add a new Specialization entity to the database.

        Args:
            specialization (Specialization): The Specialization entity to add.
        """
        query = "INSERT INTO specialization (name) VALUES (%s)"
        params = (specialization.name,)
        self.db.execute(query, params)

    @override
    def update(self, specialization: Specialization):
        """
        Update an existing Specialization entity in the database.

        Args:
            specialization (Specialization): The Specialization entity to update.
        """
        if specialization.id is None:
            self.add(specialization)
            return

        query = "UPDATE specialization SET name = %s WHERE id = %s"
        params = (specialization.name, specialization.id)
        self.db.execute(query, params)

    @override
    def delete(self, specialization: Specialization):
        """
        Delete a Specialization entity from the database.

        Args:
            specialization (Specialization): The Specialization entity to delete.
        """
        id = specialization.id
        query = "DELETE FROM specialization WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)