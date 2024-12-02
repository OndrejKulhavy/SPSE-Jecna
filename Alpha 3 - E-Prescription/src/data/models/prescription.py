from datetime import date


class Prescription:
    """
    A class to represent a Prescription.

    Methods
    -------
    None
    """

    def __init__(
            self,
            id: int,
            patient_id: int,
            issued_by_doctor_id: int,
            issued_date: date,
            valid_until: date,
            status: str,
            type: str
    ):
        """
        Constructs all the necessary attributes for the prescription object.

        Parameters
        ----------
            id : int
                unique identifier for the prescription
            patient_id : int
                unique identifier for the patient the prescription is for
            issued_by_doctor_id : int
                unique identifier for the doctor who issued the prescription
            issued_date : date
                date when the prescription was issued
            valid_until : date
                date until which the prescription is valid
            status : str
                status of the prescription (e.g., 'active', 'expired')
            type : str
                type of the prescription (e.g., 'medication', 'therapy')
        """
        if id < 0 or patient_id < 0 or issued_by_doctor_id < 0:
            raise ValueError("Id values cannot be negative!")

        self.id = id
        self.patient_id = patient_id
        self.issued_by_doctor_id = issued_by_doctor_id
        self.issued_date = issued_date
        self.valid_until = valid_until
        self.status = status
        self.type = type
