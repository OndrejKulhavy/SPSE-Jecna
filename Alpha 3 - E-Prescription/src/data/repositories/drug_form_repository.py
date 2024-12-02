from typing import override

from src.data.models.drug_form import DrugForm
from src.data.repositories.base_repository import BaseRepository


class DrugFormRepo(BaseRepository):
    """
    The DrugFormRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the DrugForm model. It includes methods for
    getting all drug forms, getting a drug form by ID, adding a new drug form, updating an existing drug form,
    and deleting a drug form.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db):
        """
        The constructor for the DrugFormRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all drug forms from the database.

        Returns:
            list: A list of DrugForm objects.
        """
        query = "SELECT * FROM drug_form"
        result = self.db.fetch(query)
        return [DrugForm(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Method to get a drug form by its ID from the database.

        Parameters:
            id (int): The ID of the drug form to retrieve.

        Returns:
            DrugForm: A DrugForm object if found, None otherwise.
        """
        query = "SELECT * FROM drug_form WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return DrugForm(*result)

    @override
    def add(self, drug_form: DrugForm):
        """
        Method to add a new drug form to the database.

        Parameters:
            drug_form (DrugForm): The DrugForm object to add to the database.
        """
        query = "INSERT INTO drug_form (name) VALUES (%s)"
        params = (drug_form.name,)
        self.db.execute(query, params)

    @override
    def update(self, drug_form: DrugForm):
        """
        Method to update an existing drug form in the database.

        If the drug form does not have an ID, it is added to the database.

        Parameters:
            drug_form (DrugForm): The DrugForm object to update in the database.
        """
        if drug_form.id is None:
            self.add(drug_form)
            return

        query = "UPDATE drug_form SET name = %s WHERE id = %s"
        params = (drug_form.name, drug_form.id)
        self.db.execute(query, params)

    @override
    def delete(self, drug_form: DrugForm):
        """
        Method to delete a drug form from the database.

        Parameters:
            drug_form (DrugForm): The DrugForm object to delete from the database.
        """
        id = drug_form.id
        query = "DELETE FROM drug_form WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)