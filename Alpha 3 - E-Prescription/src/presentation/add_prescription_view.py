from datetime import datetime

import customtkinter
from CTkMessagebox import CTkMessagebox

from src.data.models.prescription import Prescription
from src.data.models.prescription_item import PrescriptionItem


class AddPrescriptionView(customtkinter.CTkToplevel):
    """
    A class used to manage the Add Prescription view.

    ...

    Attributes
    ----------
    app : App
        an instance of the App class which manages the application
    doctor : Doctor
        the currently logged in doctor
    patients : List[Patient]
        a list of patients
    drugs : List[Drug]
        a list of drugs

    Methods
    -------
    create_widgets()
        Creates the widgets for the view.
    add_prescription()
        Adds a new prescription.
    """

    def __init__(self, patients, drugs, app):
        """
        Constructs all the necessary attributes for the AddPrescriptionView object.

        Parameters
        ----------
            patients : List[Patient]
                a list of patients
            drugs : List[Drug]
                a list of drugs
            app : App
                an instance of the App class which manages the application
        """

        super().__init__()
        self.app = app
        self.doctor = app.logged_in_user
        self.patients = patients
        self.drugs = drugs
        self.title("Add Prescription")
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the view.

        Returns
        -------
            None
        """

        self.patient_label = customtkinter.CTkLabel(self, text="Patient:")
        self.patient_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.patient_entry = customtkinter.CTkComboBox(self, values=[str(patient) for patient in self.patients])
        self.patient_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.status_label = customtkinter.CTkLabel(self, text="Status:")
        self.status_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.status_entry = customtkinter.CTkComboBox(self, values=['vydaný', 'zrušený', 'použitý'])
        self.status_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.type_label = customtkinter.CTkLabel(self, text="Type:")
        self.type_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.type_entry = customtkinter.CTkComboBox(self, values=['běžné', 'pohotovostní', 'náhradní', 'dlouhodobé'])
        self.type_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.valid_until_label = customtkinter.CTkLabel(self, text="Valid Until:")
        self.valid_until_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.valid_until_entry = customtkinter.CTkEntry(self, placeholder_text="YYYY-MM-DD")
        self.valid_until_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.drug_label = customtkinter.CTkLabel(self, text="Drug:")
        self.drug_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.drug_entry = customtkinter.CTkComboBox(self, values=[drug.name for drug in self.drugs])
        self.drug_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.quantity_label = customtkinter.CTkLabel(self, text="Quantity:")
        self.quantity_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.quantity_entry = customtkinter.CTkEntry(self)
        self.quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.dosage_label = customtkinter.CTkLabel(self, text="Dosage:")
        self.dosage_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.dosage_entry = customtkinter.CTkEntry(self)
        self.dosage_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.instructions_label = customtkinter.CTkLabel(self, text="Instructions:")
        self.instructions_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.instructions_entry = customtkinter.CTkEntry(self)
        self.instructions_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.add_prescription_button = customtkinter.CTkButton(self, text="Add Prescription",
                                                               command=self.add_prescription)
        self.add_prescription_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_prescription(self):
        """
        Adds a new prescription.

        Returns
        -------
            None

        Raises
        ------
            ValueError
                If some fields are invalid
            Exception
                If an unexpected error occurred
        """
        try:
            patient_id = next(patient.id for patient in self.patients if str(patient) == self.patient_entry.get())
            status = self.status_entry.get()
            type = self.type_entry.get()
            valid_until = self.valid_until_entry.get()
            drug_id = next(drug.id for drug in self.drugs if drug.name == self.drug_entry.get())
            quantity = self.quantity_entry.get()
            dosage = self.dosage_entry.get()
            instructions = self.instructions_entry.get()

            prescription = Prescription(
                id=0,
                patient_id=patient_id,
                issued_by_doctor_id=self.doctor.id,
                issued_date=datetime.now().date(),
                valid_until=datetime.strptime(valid_until, "%Y-%m-%d").date(),
                status=status,
                type=type
            )

            prescription_item = PrescriptionItem(
                id=0,
                prescription_id=0,
                drug_id=drug_id,
                quantity=int(quantity),
                dosage=dosage,
                instructions=instructions,
                picked_up=False
            )
            print(patient_id)
            self.app.create_prescription_event(prescription, prescription_item)
            CTkMessagebox(
                title="Success",
                message="Prescription added successfully!",
                icon="info"
            )
            self.withdraw()
        except ValueError as e:
            CTkMessagebox(
                title="Invalid inputs",
                message=f"Some fields are invalid Make sure to fill all fields correctly! Error message: {e}",
                icon="cancel"
            )
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"An error occurred while adding the prescription. Error message: {e}",
                icon="error"
            )
