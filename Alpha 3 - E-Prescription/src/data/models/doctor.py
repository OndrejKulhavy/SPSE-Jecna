from passlib.hash import pbkdf2_sha256


class Doctor:
    def __init__(
            self,
            id: int,
            title: str,
            first_name: str,
            middle_name: str,
            last_name: str,
            phone: str,
            email: str,
            specialization_id: int,
            date_of_birth: str,
            password_hash: str
    ):
        """
        Initialize a Doctor object with the specified attributes.

        Args:
            id (int): Unique identifier for the doctor.
            title (str): Title of the doctor (e.g., Dr.).
            first_name (str): First name of the doctor.
            middle_name (str): Middle name of the doctor.
            last_name (str): Last name of the doctor.
            phone (str): Phone number of the doctor.
            email (str): Email address of the doctor.
            specialization_id (int): Unique identifier for the doctor's specialization.
            date_of_birth (str): Date of birth of the doctor (format: 'YYYY-MM-DD').
            password_hash (str): Hashed password using pbkdf2_sha256.

        Raises:
            ValueError: If id or specialization_id is negative.
        """
        if id < 0 or specialization_id < 0:
            raise ValueError("Id value and specialization_id cannot be negative!")

        self.id = id
        self.title = title
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.specialization_id = specialization_id
        self.date_of_birth = date_of_birth
        self.password_hash = password_hash

    def verify_password(self, password):
        """
        Verify if the provided password matches the stored hashed password.

        Args:
            password (str): Password to be verified.

        Returns:
            bool: True if the password is correct, False otherwise.
        """
        return pbkdf2_sha256.verify(password, self.password_hash)

    def __str__(self):
        """
        Returns a string representation of the doctor.

        Returns:
            str: String representation in the format "{title} {first_name} {last_name}".
        """
        return f"{self.title} {self.first_name} {self.last_name}"
