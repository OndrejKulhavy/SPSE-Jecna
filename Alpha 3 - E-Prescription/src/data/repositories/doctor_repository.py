from typing import override

from src.data.db_manager import DatabaseManager
from src.data.models.doctor import Doctor
from src.data.repositories.base_repository import BaseRepository


class DoctorRepo(BaseRepository):
    """
    The DoctorRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the Doctor model. It includes methods for
    getting all doctors, getting a doctor by ID, getting a doctor by email, adding a new doctor, updating an existing doctor,
    and deleting a doctor.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db: DatabaseManager):
        """
        The constructor for the DoctorRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all doctors from the database.

        Returns:
            list: A list of Doctor objects.
        """
        query = "SELECT * FROM doctor"
        result = self.db.fetch(query)
        return [Doctor(*row) for row in result]

    @override
    def get_by_id(self, id):
        """
        Method to get a doctor by its ID from the database.

        Parameters:
            id (int): The ID of the doctor to retrieve.

        Returns:
            Doctor: A Doctor object if found, None otherwise.
        """
        query = "SELECT * FROM doctor WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Doctor(*result)

    def get_by_email(self, email):
        """
        Method to get a doctor by its email from the database.

        Parameters:
            email (str): The email of the doctor to retrieve.

        Returns:
            Doctor: A Doctor object if found, None otherwise.
        """
        query = "SELECT * FROM doctor WHERE email = %s"
        params = (email,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Doctor(*result)

    @override
    def add(self, doctor: Doctor):
        """
        Method to add a new doctor to the database.

        Parameters:
            doctor (Doctor): The Doctor object to add to the database.
        """
        query = """
        INSERT INTO doctor (title, first_name, middle_name, last_name, phone, email, specialization_id, date_of_birth, password_hash)
        VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (doctor.title, doctor.first_name, doctor.middle_name, doctor.last_name, doctor.phone, doctor.email,
                  doctor.specialization_id, doctor.password_hash)
        self.db.execute(query, params)

    @override
    def update(self, doctor: Doctor):
        """
        Method to update an existing doctor in the database.

        If the doctor does not have an ID, it is added to the database.

        Parameters:
            doctor (Doctor): The Doctor object to update in the database.
        """
        if doctor.id is None:
            self.add(doctor)
            return

        query = """
        UPDATE doctor
        SET title = %s, first_name = %s, middle_name = %s, last_name = %s, phone = %s, email = %s, specialization_id = %s, password_hash = %s
        WHERE id = %s"""
        params = (doctor.title, doctor.first_name, doctor.middle_name, doctor.last_name, doctor.phone, doctor.email,
                  doctor.specialization_id, doctor.password_hash, doctor.id)
        self.db.execute(query, params)

    @override
    def delete(self, doctor: Doctor):
        """
        Method to delete a doctor from the database.

        Parameters:
            doctor (Doctor): The Doctor object to delete from the database.
        """
        id = doctor.id
        query = "DELETE FROM doctor WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
