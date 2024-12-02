class DrugForm:
    def __init__(
            self,
            id: int,
            name: str
    ):
        """
        Initialize a DrugForm object with the specified attributes.

        Args:
            id (int): Unique identifier for the drug form.
            name (str): Name of the drug form.

        Raises:
            ValueError: If id is negative.
        """
        if id < 0:
            raise ValueError("Id value cannot be negative!")

        self.id = id
        self.name = name
