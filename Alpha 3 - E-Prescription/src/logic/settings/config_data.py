import configparser
from collections import namedtuple


class Settings:
    """
    A class used to manage the application settings.

    ...

    Attributes
    ----------
    CONFIG_FILE_NAME : str
        the name of the configuration file

    Methods
    -------
    get_database_settings()
        Retrieves the database settings from the configuration file.
    __get_settings(section: str, parameters: List[str])
        Retrieves the settings for a specific section from the configuration file.
    """

    CONFIG_FILE_NAME = "config.ini"

    @staticmethod
    def get_database_settings():
        """
        Retrieves the database settings from the configuration file.

        Returns
        -------
            namedtuple
                a named tuple containing the database settings
        """
        section = "database"
        parameters = ['host', 'user', 'password', 'schema']
        return Settings.__get_settings(section, parameters)

    @staticmethod
    def __get_settings(section, parameters):
        """
        Retrieves the settings for a specific section from the configuration file.

        Parameters
        ----------
            section : str
                the section in the configuration file
            parameters : List[str]
                the parameters to retrieve from the section

        Returns
        -------
            namedtuple
                a named tuple containing the settings

        Raises
        ------
            ValueError
                If the section or any of the parameters are not found in the configuration file
        """
        config = configparser.ConfigParser()
        config.read(Settings.CONFIG_FILE_NAME)

        if section not in config.sections():
            raise ValueError(f"Section {section} not found in config file")

        settings = namedtuple(f"{section.capitalize()}Settings", parameters)

        for parameter in parameters:
            if config[section][parameter] is None:
                raise ValueError(f"Parameter {parameter} not found in section {section} in config file")

            setattr(settings, parameter, config[section][parameter])

        return settings
