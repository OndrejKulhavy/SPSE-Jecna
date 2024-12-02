import json

from src.data.db_manager import DatabaseManager


class DbImporter:
    """
    A class used to import data into a database.

    ...

    Attributes
    ----------
    db : DatabaseManager
        an instance of the DatabaseManager class which manages the database connection

    Methods
    -------
    import_csv_data(path: str)
        Imports data from a CSV file into the database.
    """

    def __init__(self, db_connection: DatabaseManager):
        """
        Constructs all the necessary attributes for the DbImporter object.

        Parameters
        ----------
            db_connection : DatabaseManager
                an instance of the DatabaseManager class which manages the database connection
        """
        self.db = db_connection

    def import_csv_data(self, path: str):
        """
        Imports data from a CSV file into the database.

        Parameters
        ----------
            path : str
                the path to the CSV file

        Raises
        ------
            NotImplementedError
                If this method is not implemented
        """
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            NotImplementedError('Implement this method')
