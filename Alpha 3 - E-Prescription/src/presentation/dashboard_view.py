import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

from src.data.repositories.patient_repository import PatientRepo
from src.data.repositories.prescription_repository import PrescriptionRepo


class DashboardView(customtkinter.CTkToplevel):
    """
    A class used to manage the Dashboard view.

    ...

    Attributes
    ----------
    app : App
        an instance of the App class which manages the application

    Methods
    -------
    __init__(app: App)
        Constructs all the necessary attributes for the DashboardView object.
    __load_prescription_history()
        Loads the prescription history for the logged in user.
    open_prescription(prescription: Prescription)
        Opens the prescription view for a specific prescription.
    print_prescription(prescription: Prescription)
        Prints a specific prescription.
    create_prescription()
        Opens the create prescription view.
    """

    def __init__(self, app):
        """
        Constructs all the necessary attributes for the DashboardView object.

        Parameters
        ----------
            app : App
                an instance of the App class which manages the application
        """
        super().__init__()
        self.title("Dashboard")
        self.geometry(f"{1100}x{580}")
        self.app = app
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        image = customtkinter.CTkImage(Image.open("./resources/social_preview_wbg.png"),
                                       size=(238, 116))

        self.image_label = customtkinter.CTkLabel(self.sidebar_frame)
        self.image_label.configure(self.sidebar_frame, image=image, text="")
        self.image_label.image = image
        self.image_label.grid(row=0, column=0)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Create Prescription",
                                                        command=self.create_prescription)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=(0, 30), sticky="ew")

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add Patient",
                                                        command=self.app.open_add_patient_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Add Drug",
                                                        command=self.app.open_add_drug_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.username_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                     text=f"Logged in as: {self.app.logged_in_user}")
        self.username_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.logout_button = customtkinter.CTkButton(self.sidebar_frame, text="Log Out")
        self.logout_button.grid(row=6, column=0, padx=20, pady=(0, 20))

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="History of prescriptions")
        self.scrollable_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.__load_prescription_history()

    def __load_prescription_history(self):
        """
        Loads the prescription history for the logged in user.

        Returns
        -------
            None
        """
        prescription_history = self.app.load_prescription_history()

        for i, prescription in enumerate(prescription_history):
            prescription_name = f"Prescription for {prescription.patient.first_name} {prescription.patient.last_name} issued on {prescription.prescription.issued_date}"

            prescription_label = customtkinter.CTkLabel(self.scrollable_frame, text=prescription_name)
            prescription_label.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="nsew")
            prescription_label.configure(anchor="w")

            open_button = customtkinter.CTkButton(self.scrollable_frame, text="Open",
                                                  command=lambda p=prescription: self.open_prescription(p.prescription))
            open_button.grid(row=i, column=1, padx=10, pady=(0, 20), sticky="nsew")

            print_button = customtkinter.CTkButton(self.scrollable_frame, text="Print Report",
                                                   command=lambda p=prescription: self.print_prescription(
                                                       p.prescription))
            print_button.grid(row=i, column=2, padx=10, pady=(0, 20), sticky="nsew")

    def open_prescription(self, prescription):
        """
        Opens the prescription view for a specific prescription.

        Parameters
        ----------
            prescription : Prescription
                the prescription to view

        Returns
        -------
            None

        Raises
        ------
            Exception
                If an unexpected error occurred
        """
        try:
            self.app.open_prescription_event(prescription)
        except Exception as e:
            CTkMessagebox(title="Error", message=f"An unexpected error occurred ({e})", icon="cancel")

    def print_prescription(self, prescription):
        """
        Prints a specific prescription.

        Parameters
        ----------
            prescription : Prescription
                the prescription to print

        Returns
        -------
            None

        Raises
        ------
            Exception
                If an unexpected error occurred
        """
        try:
            self.app.print_prescription_event(prescription)
        except Exception as e:
            CTkMessagebox(title="Error", message=f"An unexpected error occurred ({e})", icon="cancel")

    def create_prescription(self):
        """
        Opens the create prescription view.

        Returns
        -------
            None

        Raises
        ------
            ValueError
                If an unexpected error occurred
        """
        try:
            self.app.open_create_prescription_event()
        except ValueError as e:
            CTkMessagebox(title="Error", message=f"An unexpected error occurred ({e})", icon="cancel")
