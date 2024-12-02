class PrescriptionItem:
    """
    A class to represent a Prescription Item.
    """

    def __init__(
            self,
            id: int,
            prescription_id: int,
            drug_id: int,
            quantity: int,
            dosage: str,
            instructions: str,
            picked_up: bool
    ):
        """
        Constructs all the necessary attributes for the prescription item object.

        Parameters
        ----------
            id : int
                unique identifier for the prescription item
            prescription_id : int
                unique identifier for the prescription the item is part of
            drug_id : int
                unique identifier for the drug prescribed
            quantity : int
                quantity of the drug prescribed
            dosage : str
                dosage of the drug prescribed
            instructions : str
                instructions for the use of the drug
            picked_up : bool
                indicates whether the prescription item has been picked up by the patient
        """
        if id < 0 or prescription_id < 0 or drug_id < 0:
            raise ValueError("Id values cannot be negative!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.id = id
        self.prescription_id = prescription_id
        self.drug_id = drug_id
        self.quantity = quantity
        self.dosage = dosage
        self.instructions = instructions
        self.picked_up = picked_up