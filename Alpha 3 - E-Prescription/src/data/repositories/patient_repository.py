from typing import override

from src.data.models.patient import Patient
from src.data.repositories.base_repository import BaseRepository


class PatientRepo(BaseRepository):
    """
    The PatientRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the Patient model. It includes methods for
    getting all patients, getting a patient by ID, adding a new patient, updating an existing patient,
    and deleting a patient.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db):
        """
        The constructor for the PatientRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all patients from the database.

        Returns:
            list: A list of Patient objects.
        """
        query = "SELECT * FROM patient"
        result = self.db.fetch(query)
        return [Patient(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Method to get a patient by its ID from the database.

        Parameters:
            id (int): The ID of the patient to retrieve.

        Returns:
            Patient: A Patient object if found, None otherwise.
        """
        query = "SELECT * FROM patient WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Patient(*result)

    @override
    def add(self, patient: Patient):
        """
        Method to add a new patient to the database.

        Parameters:
            patient (Patient): The Patient object to add to the database.
        """
        query = (
            "INSERT INTO patient (phone, email, street, house, city, psc, insurance_company_id, date_of_birth, first_name, middle_name, last_name) "
            "VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        params = (
            patient.phone, patient.email, patient.street, patient.house, patient.city, patient.psc,
            patient.insurance_company_id, patient.date_of_birth, patient.first_name, patient.middle_name,
            patient.last_name)
        self.db.execute(query, params)

    @override
    def update(self, patient: Patient):
        """
        Method to update an existing patient in the database.

        If the patient does not have an ID, it is added to the database.

        Parameters:
            patient (Patient): The Patient object to update in the database.
        """
        if patient.id is None:
            self.add(patient)
            return

        query = "UPDATE patient SET first_name = %s, middle_name = %s, last_name = %s, phone = %s, email = %s, street = %s, house = %s, city = %s, psc = %s, insurance_company_id = %s WHERE id = %s"
        params = (
            patient.first_name, patient.middle_name, patient.last_name, patient.phone, patient.email, patient.street,
            patient.house, patient.city, patient.psc, patient.insurance_company_id, patient.id)
        self.db.execute(query, params)

    @override
    def delete(self, patient: Patient):
        """
        Method to delete a patient from the database.

        Parameters:
            patient (Patient): The Patient object to delete from the database.
        """
        id = patient.id
        query = "DELETE FROM patient WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)