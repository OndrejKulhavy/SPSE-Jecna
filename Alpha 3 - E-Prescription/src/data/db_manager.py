import mysql.connector

from src.logic.settings.config_data import Settings


class DatabaseManager:
    """
    A class used to manage the database connection and execute SQL queries.

    ...

    Attributes
    ----------
    connection : mysql.connector.connection
        the active database connection

    Methods
    -------
    connect()
        Establishes a connection to the database using the settings from the Settings class.
    disconnect()
        Closes the active database connection.
    execute(query: str, params: Optional[Tuple])
        Executes a SQL query with optional parameters and commits the changes.
    fetch(query: str, params: Optional[Tuple])
        Executes a SQL query with optional parameters and fetches all the results.
    fetch_one(query: str, params: Optional[Tuple])
        Executes a SQL query with optional parameters and fetches the first result.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the DatabaseManager object and connects to the database.
        """
        self.connection = None
        self.connect()

    def connect(self):
        """
        Establishes a connection to the database using the settings from the Settings class.
        """
        settings = Settings.get_database_settings()
        self.connection = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            database=settings.schema
        )

    def disconnect(self):
        """
        Closes the active database connection.
        """
        self.connection.close()

    def execute(self, query, params=None):
        """
        Executes a SQL query with optional parameters and commits the changes.

        Parameters
        ----------
            query : str
                the SQL query to execute
            params : Optional[Tuple]
                the parameters to use in the SQL query

        Returns
        -------
            int
                the ID of the last row affected by the query
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()
        return cursor.lastrowid

    def fetch(self, query, params=None):
        """
        Executes a SQL query with optional parameters and fetches all the results.

        Parameters
        ----------
            query : str
                the SQL query to execute
            params : Optional[Tuple]
                the parameters to use in the SQL query

        Returns
        -------
            List[Tuple]
                a list of tuples representing the rows fetched from the database
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_one(self, query, params=None) -> object:
        """
        Executes a SQL query with optional parameters and fetches the first result.

        Parameters
        ----------
            query : str
                the SQL query to execute
            params : Optional[Tuple]
                the parameters to use in the SQL query

        Returns
        -------
            Tuple
                a tuple representing the first row fetched from the database
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result
