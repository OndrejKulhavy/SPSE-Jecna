from typing import override

from src.data.models.drug import Drug
from src.data.repositories.base_repository import BaseRepository


class DrugRepo(BaseRepository):
    """
    The DrugRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the Drug model. It includes methods for
    getting all drugs, getting a drug by ID, adding a new drug, updating an existing drug,
    and deleting a drug.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db):
        """
        The constructor for the DrugRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all drugs from the database.

        Returns:
            list: A list of Drug objects.
        """
        query = "SELECT * FROM drug"
        result = self.db.fetch(query)
        return [Drug(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Method to get a drug by its ID from the database.

        Parameters:
            id (int): The ID of the drug to retrieve.

        Returns:
            Drug: A Drug object if found, None otherwise.
        """
        query = "SELECT * FROM drug WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Drug(*result)

    @override
    def add(self, drug: Drug):
        """
        Method to add a new drug to the database.

        Parameters:
            drug (Drug): The Drug object to add to the database.
        """
        query = "INSERT INTO drug (name, price, active_substance, form, description, side_effects, storage_conditions) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (drug.name, drug.price, drug.active_substance, drug.form, drug.description,
                  drug.side_effects, drug.storage_conditions)
        self.db.execute(query, params)

    @override
    def update(self, drug: Drug):
        """
        Method to update an existing drug in the database.

        If the drug does not have an ID, it is added to the database.

        Parameters:
            drug (Drug): The Drug object to update in the database.
        """
        if drug.id is None:
            self.add(drug)
            return

        query = "UPDATE drug SET name = %s, price = %s, active_substance = %s, form = %s, description = %s, " \
                "side_effects = %s, storage_conditions = %s WHERE id = %s"
        params = (drug.name, drug.price, drug.active_substance, drug.form, drug.description,
                  drug.side_effects, drug.storage_conditions, drug.id)
        self.db.execute(query, params)

    @override
    def delete(self, drug: Drug):
        """
        Method to delete a drug from the database.

        Parameters:
            drug (Drug): The Drug object to delete from the database.
        """
        id = drug.id
        query = "DELETE FROM drug WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)