import customtkinter

from src.data.models.prescription import Prescription


class PrescriptionView(customtkinter.CTkToplevel):
    """
    A class used to manage the Prescription view.

    ...

    Attributes
    ----------
    prescription : Prescription
        the prescription to view
    patient : Patient
        the patient associated with the prescription
    drugs : List[Drug]
        a list of drugs associated with the prescription

    Methods
    -------
    __init__(prescription: Prescription, patient: Patient, drugs: List[Drug])
        Constructs all the necessary attributes for the PrescriptionView object.
    """

    def __init__(self, prescription: Prescription, patient, drugs):
        """
        Constructs all the necessary attributes for the PrescriptionView object.

        Parameters
        ----------
            prescription : Prescription
                the prescription to view
            patient : Patient
                the patient associated with the prescription
            drugs : List[Drug]
                a list of drugs associated with the prescription
        """
        super().__init__()

        self.title("Prescription Details")
        self.resizable(False, False)

        labels = ["Patient first name", "Patient last name", "Issued Date:", "Valid Until:", "Type:"]
        values = [patient.first_name, patient.last_name, prescription.issued_date,
                  prescription.valid_until, prescription.type]

        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(self, text=label_text)
            label.grid(row=i, column=0, sticky="w", padx=5, pady=5)

            text_variable = customtkinter.StringVar(value=str(values[i]))
            text_box = customtkinter.CTkEntry(self, textvariable=text_variable, state='readonly')
            text_box.grid(row=i, column=1, padx=5, pady=5)
        # Add an empty row
        self.grid_rowconfigure(len(labels), weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="List of drugs prescribed:")
        self.scrollable_frame.grid(row=len(labels) + 1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        for i, drug in enumerate(drugs):
            drug_name = f"{drug.name} - {drug.active_substance}"
            drug_label = customtkinter.CTkLabel(self.scrollable_frame, text=drug_name, anchor="w")
            drug_label.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="nsew")
