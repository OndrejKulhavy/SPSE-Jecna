class Drug:
    def __init__(
            self,
            id: int,
            name: str,
            price: float,
            active_substance: str,
            form: int,
            description: str,
            side_effects: str,
            storage_conditions: str
    ):
        """
        Initialize a Drug object with the specified attributes.

        Args:
            id (int): Unique identifier for the drug.
            name (str): Name of the drug.
            price (float): Price of the drug.
            active_substance (str): Active substance in the drug.
            form (int): Form of the drug (e.g., tablet, liquid).
            description (str): Description of the drug.
            side_effects (str): Information about side effects of the drug.
            storage_conditions (str): Recommended storage conditions for the drug.

        Raises:
            ValueError: If id or form is negative.
        """
        if id < 0 or form < 0:
            raise ValueError("Id value and form cannot be negative!")

        self.id = id
        self.name = name
        self.price = price
        self.active_substance = active_substance
        self.form = form
        self.description = description
        self.side_effects = side_effects
        self.storage_conditions = storage_conditions
