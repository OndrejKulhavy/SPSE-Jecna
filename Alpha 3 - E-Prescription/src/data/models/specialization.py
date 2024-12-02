class Specialization:
    """
    A class to represent a Specialization.

    ...

    Attributes
    ----------
    id : int
        unique identifier for the specialization
    name : str
        name of the specialization
    """

    def __init__(
            self,
            id: int,
            name: str
    ):
        """
        Constructs all the necessary attributes for the specialization object.

        Parameters
        ----------
            id : int
                unique identifier for the specialization
            name : str
                name of the specialization
        """
        if id < 0:
            raise ValueError("Id cannot be negative!")

        self.id = id
        self.name = name
