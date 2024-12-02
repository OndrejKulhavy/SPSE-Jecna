from typing import override

from src.data.db_manager import DatabaseManager
from src.data.models.insurance_company import InsuranceCompany
from src.data.repositories.base_repository import BaseRepository


class InsuranceCompanyRepo(BaseRepository):
    """
    The InsuranceCompanyRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the InsuranceCompany model. It includes methods for
    getting all insurance companies, getting an insurance company by ID, adding a new insurance company, updating an existing insurance company,
    and deleting an insurance company.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db: DatabaseManager):
        """
        The constructor for the InsuranceCompanyRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all insurance companies from the database.

        Returns:
            list: A list of InsuranceCompany objects.
        """
        query = "SELECT * FROM insurance_company"
        result = self.db.fetch(query)
        return [InsuranceCompany(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Method to get an insurance company by its ID from the database.

        Parameters:
            id (int): The ID of the insurance company to retrieve.

        Returns:
            InsuranceCompany: An InsuranceCompany object if found, None otherwise.
        """
        query = "SELECT * FROM insurance_company WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return InsuranceCompany(*result)

    @override
    def add(self, insurance_company: InsuranceCompany):
        """
        Method to add a new insurance company to the database.

        Parameters:
            insurance_company (InsuranceCompany): The InsuranceCompany object to add to the database.
        """
        query = "INSERT INTO insurance_company (id, code, abbreviation, name, street, house, city, psc) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            insurance_company.id, insurance_company.code, insurance_company.abbreviation, insurance_company.name,
            insurance_company.street, insurance_company.house, insurance_company.city,
            insurance_company.psc)
        self.db.execute(query, values)

    @override
    def update(self, insurance_company: InsuranceCompany):
        """
        Method to update an existing insurance company in the database.

        If the insurance company does not have an ID, it is added to the database.

        Parameters:
            insurance_company (InsuranceCompany): The InsuranceCompany object to update in the database.
        """
        if insurance_company.id is None:
            self.add(insurance_company)
            return

        query = "UPDATE insurance_company SET code = %s, abbreviation = %s, name = %s, street = %s, house = %s, " \
                "city = %s, psc = %s WHERE id = %s"
        values = (
            insurance_company.code, insurance_company.abbreviation, insurance_company.name, insurance_company.street,
            insurance_company.house, insurance_company.city, insurance_company.psc, insurance_company.id)
        self.db.execute(query, values)

    @override
    def delete(self, insurance_company: InsuranceCompany):
        """
        Method to delete an insurance company from the database.

        Parameters:
            insurance_company (InsuranceCompany): The InsuranceCompany object to delete from the database.
        """
        id = insurance_company.id
        query = "DELETE FROM insurance_company WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
