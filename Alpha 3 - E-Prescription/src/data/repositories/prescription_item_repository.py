from typing import override

from src.data.models.prescription import Prescription
from src.data.models.prescription_item import PrescriptionItem
from src.data.repositories.base_repository import BaseRepository


class PrescriptionItemRepo(BaseRepository):
    """
    The PrescriptionItemRepo class that inherits from the BaseRepository class.

    This class provides the specific implementation of the BaseRepository for the PrescriptionItem model. It includes methods for
    getting all prescription items, getting a prescription item by ID, getting prescription items by prescription, adding a new prescription item,
    updating an existing prescription item, and deleting a prescription item.

    Attributes:
        db (DatabaseManager): The database manager that will be used to interact with the database.
    """

    def __init__(self, db):
        """
        The constructor for the PrescriptionItemRepo class.

        Parameters:
            db (DatabaseManager): The database manager that will be used to interact with the database.
        """
        super().__init__(db)

    @override
    def get_all(self):
        """
        Method to get all prescription items from the database.

        Returns:
            list: A list of PrescriptionItem objects.
        """
        query = "SELECT * FROM prescription_item"
        result = self.db.fetch(query)
        return [PrescriptionItem(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        """
        Method to get a prescription item by its ID from the database.

        Parameters:
            id (int): The ID of the prescription item to retrieve.

        Returns:
            PrescriptionItem: A PrescriptionItem object if found, None otherwise.
        """
        query = "SELECT * FROM prescription_item WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return PrescriptionItem(*result)

    def get_by_prescription(self, prescription: Prescription):
        """
        Method to get prescription items by prescription from the database.

        Parameters:
            prescription (Prescription): The Prescription object to retrieve items for.

        Returns:
            list: A list of PrescriptionItem objects.
        """
        id = prescription.id
        query = "SELECT * FROM prescription_item WHERE prescription_id = %s"
        params = (id,)
        result = self.db.fetch(query, params)
        return [PrescriptionItem(*row) for row in result]

    @override
    def add(self, prescription_item: PrescriptionItem):
        """
        Method to add a new prescription item to the database.

        Parameters:
            prescription_item (PrescriptionItem): The PrescriptionItem object to add to the database.
        """
        query = "INSERT INTO prescription_item (prescription_id, drug_id, quantity, dosage, instructions, picked_up) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        params = (prescription_item.prescription_id, prescription_item.drug_id, prescription_item.quantity,
                  prescription_item.dosage, prescription_item.instructions, prescription_item.picked_up)
        self.db.execute(query, params)

    @override
    def update(self, prescription_item: PrescriptionItem):
        """
        Method to update an existing prescription item in the database.

        If the prescription item does not have an ID, it is added to the database.

        Parameters:
            prescription_item (PrescriptionItem): The PrescriptionItem object to update in the database.
        """
        if prescription_item.id is None:
            self.add(prescription_item)
            return
        query = "UPDATE prescription_item SET prescription_id = %s, drug_id = %s, quantity = %s, dosage = %s, " \
                "instructions = %s, picked_up = %s WHERE id = %s"
        params = (prescription_item.prescription_id, prescription_item.drug_id, prescription_item.quantity,
                  prescription_item.dosage, prescription_item.instructions,
                  prescription_item.picked_up, prescription_item.id)
        self.db.execute(query, params)

    @override
    def delete(self, prescription_item: PrescriptionItem):
        """
        Method to delete a prescription item from the database.

        Parameters:
            prescription_item (PrescriptionItem): The PrescriptionItem object to delete from the database.
        """
        id = prescription_item.id
        query = "DELETE FROM prescription_item WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)