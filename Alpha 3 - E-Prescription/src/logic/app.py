from collections import namedtuple

from src.data.repositories.doctor_repository import DoctorRepo
from src.data.repositories.drug_form_repository import DrugFormRepo
from src.data.repositories.drug_repository import DrugRepo
from src.data.repositories.insurance_company_repository import InsuranceCompanyRepo
from src.data.repositories.patient_repository import PatientRepo
from src.data.repositories.prescription_item_repository import PrescriptionItemRepo
from src.data.repositories.prescription_repository import PrescriptionRepo
from src.logic.report.report_generator import ReportGenerator
from src.presentation.add_drug_view import AddDrugView
from src.presentation.add_patient_view import AddPatientView
from src.presentation.add_prescription_view import AddPrescriptionView
from src.presentation.dashboard_view import DashboardView
from src.presentation.login_view import LoginView
from src.presentation.prescription_view import PrescriptionView


class App:
    """
    A class used to manage the application.

    ...

    Attributes
    ----------
    db : DatabaseManager
        an instance of the DatabaseManager class which manages the database connection
    logged_in_user : Doctor
        the currently logged in user
    dashboard : DashboardView
        the dashboard view
    """

    def __init__(self, db):
        """
        Constructs all the necessary attributes for the App object.

        Parameters
        ----------
            db : DatabaseManager
                an instance of the DatabaseManager class which manages the database connection
        """
        self.db = db
        self.logged_in_user = None
        self.dashboard = None
        self.authenticate()

    def authenticate(self):
        """
        Authenticates the user.

        Returns
        -------
            None
        """
        login_view = LoginView(app=self)
        login_view.mainloop()

    def initialize_dashboard(self):
        """
        Initializes the dashboard view.

        Returns
        -------
            None
        """
        self.dashboard = DashboardView(self)

    def load_prescription_history(self):
        """
        Loads the prescription history for the logged in user.

        Returns
        -------
            List[PrescriptionHistoryEntry]
                a list of prescription history entries
        """
        PrescriptionHistoryEntry = namedtuple('PrescriptionHistoryEntry', ['prescription', 'patient'])
        history = []
        prescriptions = PrescriptionRepo(db=self.db).get_by_doctor(self.logged_in_user)
        for prescription in prescriptions:
            patient = PatientRepo(db=self.db).get_by_id(prescription.patient_id)
            history.append(PrescriptionHistoryEntry(prescription, patient))
        return history

    def login_event(self, username, password):
        """
        Handles the login event.

        Parameters
        ----------
            username : str
                the username
            password : str
                the password

        Returns
        -------
            None

        Raises
        ------
            ValueError
                If the username or password is invalid
        """
        doctor = DoctorRepo(db=self.db).get_by_email(username)

        if doctor is None or not doctor.verify_password(password):
            raise ValueError("Invalid username or password")

        self.logged_in_user = doctor
        self.initialize_dashboard()

    def logout_event(self):
        """
        Handles the logout event.

        Returns
        -------
            None
        """
        self.dashboard.destroy()
        self.logged_in_user = None
        self.authenticate()

    def open_add_patient_event(self):
        """
        Opens the add patient view.

        Returns
        -------
            None
        """
        list_of_insurance_companies = InsuranceCompanyRepo(db=self.db).get_all()
        AddPatientView(app=self, insurance_companies=list_of_insurance_companies)

    def add_patient_event(self, patient):
        """
        Adds a new patient.

        Parameters
        ----------
            patient : Patient
                the patient to add

        Returns
        -------
            None
        """
        PatientRepo(db=self.db).add(patient)

    def open_add_drug_event(self):
        """
        Opens the add drug view.

        Returns
        -------
            None
        """
        forms = DrugFormRepo(db=self.db).get_all()
        AddDrugView(app=self, forms=forms)

    def add_drug_event(self, drug):
        """
        Adds a new drug.

        Parameters
        ----------
            drug : Drug
                the drug to add

        Returns
        -------
            None
        """
        DrugRepo(db=self.db).add(drug)

    def open_create_prescription_event(self):
        """
        Opens the create prescription view.

        Returns
        -------
            None
        """
        patients = PatientRepo(db=self.db).get_all()
        drugs = DrugRepo(db=self.db).get_all()
        AddPrescriptionView(app=self, patients=patients, drugs=drugs)

    def create_prescription_event(self, prescription, item):
        """
        Creates a new prescription.

        Parameters
        ----------
            prescription : Prescription
                the prescription to create
            item : PrescriptionItem
                the prescription item to add

        Returns
        -------
            None
        """
        id = PrescriptionRepo(db=self.db).add(prescription)
        item.prescription_id = id
        PrescriptionItemRepo(db=self.db).add(item)

    def open_prescription_event(self, prescription):
        """
        Opens the prescription view.

        Parameters
        ----------
            prescription : Prescription
                the prescription to view

        Returns
        -------
            None
        """
        patient = PatientRepo(db=self.db).get_by_id(prescription.patient_id)
        items = PrescriptionItemRepo(db=self.db).get_by_prescription(prescription)
        drugs = []
        for item in items:
            drug = DrugRepo(db=self.db).get_by_id(item.drug_id)
            drugs.append(drug)
        PrescriptionView(prescription=prescription, patient=patient, drugs=drugs)

    def print_prescription_event(self, prescription):
        """
        Prints the prescription.

        Parameters
        ----------
            prescription : Prescription
                the prescription to print

        Returns
        -------
            None
        """
        ReportGenerator(db=self.db, prescription=prescription)
