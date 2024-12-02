class InsuranceCompany:
    def __init__(
            self,
            id: int,
            code: int,
            abbreviation: str,
            name: str,
            street: str,
            house: int,
            city: str,
            psc: int
    ):
        """
        Initialize an InsuranceCompany object with the specified attributes.

        Args:
            id (int): Unique identifier for the insurance company.
            code (int): Code assigned to the insurance company.
            abbreviation (str): Abbreviation or short form of the insurance company name.
            name (str): Name of the insurance company.
            street (str): Street address of the insurance company.
            house (int): House number of the insurance company.
            city (str): City where the insurance company is located.
            psc (int): Postal code (PSC) of the insurance company.

        Raises:
            ValueError: If id, code, house, or psc is negative.
        """
        if id < 0 or code < 0 or house < 0 or psc < 0:
            raise ValueError("Id, code, house, and psc values cannot be negative!")

        self.id = id
        self.code = code
        self.abbreviation = abbreviation
        self.name = name
        self.street = street
        self.house = house
        self.city = city
        self.psc = psc
