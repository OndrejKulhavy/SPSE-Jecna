from datetime import date

from src import data

class Patient:
    """
    A class to represent a Patient.

    Methods
    -------
    __str__():
        Returns the string representation of the patient.
    """

    def __init__(
            self,
            id: int,
            phone: str,
            email: str,
            street: str,
            house: int,
            city: str,
            psc: int,
            insurance_company_id: int,
            date_of_birth: date,
            first_name: str,
            middle_name: str,
            last_name: str,
    ):
        """
        Constructs all the necessary attributes for the patient object.

        Parameters
        ----------
            id : int
                unique identifier for the patient
            phone : str
                phone number of the patient
            email : str
                email address of the patient
            street : str
                street address of the patient
            house : int
                house number of the patient
            city : str
                city of the patient
            psc : int
                postal code of the patient
            insurance_company_id : int
                unique identifier for the patient's insurance company
            date_of_birth : date
                date of birth of the patient
            first_name : str
                first name of the patient
            middle_name : str
                middle name of the patient
            last_name : str
                last name of the patient
        """
        if id < 0 or insurance_company_id < 0:
            raise ValueError("Id value cannot be negative!")
        if house < 0:
            raise ValueError("House value cannot be negative!")
        if psc < 0:
            raise ValueError("PSC value cannot be negative!")

        self.id = id
        self.phone = phone
        self.email = email
        self.street = street
        self.house = house
        self.city = city
        self.psc = psc
        self.insurance_company_id = insurance_company_id
        self.date_of_birth = date_of_birth
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __str__(self):
        """
        Returns the string representation of the patient.

        Returns
        -------
        str
            a string representing the patient in the format: "first_name last_name - date_of_birth"
        """
        return f"{self.first_name} {self.last_name} - {self.date_of_birth}"