from typing import override

from src.data.models.doctor import Doctor
from src.data.models.prescription import Prescription
from src.data.repositories.base_repository import BaseRepository


class PrescriptionRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    @override
    def get_all(self):
        """Retrieve all prescriptions from the database."""
        query = "SELECT * FROM prescription"
        result = self.db.fetch(query)
        return [Prescription(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """Retrieve a prescription by its ID from the database."""
        query = "SELECT * FROM prescription WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Prescription(*result)

    def get_by_doctor(self, doctor: Doctor):
        """Retrieve all prescriptions issued by a specific doctor."""
        id = doctor.id
        query = "SELECT * FROM prescription WHERE issued_by_doctor_id = %s"
        params = (id,)
        result = self.db.fetch(query, params)
        return [Prescription(*row) for row in result]

    @override
    def add(self, prescription: Prescription):
        """Add a new prescription to the database."""
        query = "INSERT INTO prescription (patient_id, issued_by_doctor_id, issued_date, valid_until, status, type) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            prescription.patient_id, prescription.issued_by_doctor_id, prescription.issued_date,
            prescription.valid_until,
            prescription.status,
            prescription.type)
        return self.db.execute(query, params)

    @override
    def update(self, prescription: Prescription):
        """Update an existing prescription in the database."""
        if prescription.id is None:
            self.add(prescription)
            return

        query = "UPDATE prescription SET patient_id = %s, issued_by_doctor_id = %s, issued_date = %s, " \
                "valid_until = %s, status = %s, type = %s WHERE id = %s"
        params = (prescription.patient_id, prescription.issued_by_doctor_id, prescription.issued_date,
                  prescription.valid_until, prescription.status, prescription.type, prescription.id)
        self.db.execute(query, params)

    @override
    def delete(self, prescription: Prescription):
        """Delete a prescription from the database."""
        id = prescription.id
        query = "DELETE FROM prescription WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
