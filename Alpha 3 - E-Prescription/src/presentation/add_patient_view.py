from datetime import datetime

import customtkinter
from CTkMessagebox import CTkMessagebox

from src.data.models.insurance_company import InsuranceCompany
from src.data.models.patient import Patient


class AddPatientView(customtkinter.CTkToplevel):
    """
    A class used to manage the Add Patient view.

    ...

    Attributes
    ----------
    app : App
        an instance of the App class which manages the application
    insurance_companies : List[InsuranceCompany]
        a list of insurance companies

    Methods
    -------
    __add_second_tab(tabview: customtkinter.CTkTabview)
        Adds the second tab to the tab view.
    __add_first_tab(tabview: customtkinter.CTkTabview)
        Adds the first tab to the tab view.
    add_patient()
        Adds a new patient.
    """

    TAB1 = "Manually"
    TAB2 = "From File"

    def __init__(self, app, insurance_companies: [InsuranceCompany]):
        """
        Constructs all the necessary attributes for the AddPatientView object.

        Parameters
        ----------
            app : App
                an instance of the App class which manages the application
            insurance_companies : List[InsuranceCompany]
                a list of insurance companies
        """
        super().__init__()

        self.resizable(False, False)
        self.title("Add Patient")
        self.app = app
        self.insurance_companies = insurance_companies
        tabview = customtkinter.CTkTabview(self)
        tabview.pack(fill="both", expand=1)
        tabview.add(self.TAB1)
        tabview.add(self.TAB2)

        self.__add_first_tab(tabview)
        self.__add_second_tab(tabview)

    def __add_second_tab(self, tabview):
        """
        Adds the second tab to the tab view.

        Parameters
        ----------
            tabview : customtkinter.CTkTabview
                the tab view

        Returns
        -------
            None
        """
        tab = tabview.tab(self.TAB2)
        self.text_label = customtkinter.CTkLabel(tab,
                                                 text="You can add multiple persons at once by uploading a csv file.")
        self.text_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="w")

        self.file_label = customtkinter.CTkLabel(tab, text="File:")
        self.file_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.file_entry = customtkinter.CTkEntry(tab)
        self.file_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.browse_button = customtkinter.CTkButton(tab, text="Browse")
        self.browse_button.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.add_person_button_file = customtkinter.CTkButton(tab, text="Add Person")
        self.add_person_button_file.grid(row=5, column=3, columnspan=2, pady=30)

    def __add_first_tab(self, tabview):
        """
        Adds the first tab to the tab view.

        Parameters
        ----------
            tabview : customtkinter.CTkTabview
                the tab view

        Returns
        -------
            None
        """
        tab = tabview.tab(self.TAB1)
        self.first_name_label = customtkinter.CTkLabel(tab, text="Name:")
        self.first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.first_name_entry = customtkinter.CTkEntry(tab)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.middle_name_label = customtkinter.CTkLabel(tab, text="Middle Name:")
        self.middle_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.middle_name_entry = customtkinter.CTkEntry(tab)
        self.middle_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.last_name_label = customtkinter.CTkLabel(tab, text="Last Name:")
        self.last_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.last_name_entry = customtkinter.CTkEntry(tab)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.phone_label = customtkinter.CTkLabel(tab, text="Phone:")
        self.phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = customtkinter.CTkEntry(tab)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.email_label = customtkinter.CTkLabel(tab, text="Email:")
        self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = customtkinter.CTkEntry(tab)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.street_label = customtkinter.CTkLabel(tab, text="Street:")
        self.street_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.street_entry = customtkinter.CTkEntry(tab)
        self.street_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.house_label = customtkinter.CTkLabel(tab, text="House:")
        self.house_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.house_entry = customtkinter.CTkEntry(tab)
        self.house_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.city_label = customtkinter.CTkLabel(tab, text="City:")
        self.city_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.city_entry = customtkinter.CTkEntry(tab)
        self.city_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.date_of_birth_label = customtkinter.CTkLabel(tab, text="Date of Birth:")
        self.date_of_birth_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.date_of_birth_entry = customtkinter.CTkEntry(tab, placeholder_text="YYYY-MM-DD")
        self.date_of_birth_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        self.psc_label = customtkinter.CTkLabel(tab, text="Postal Code (PSC):")
        self.psc_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.psc_entry = customtkinter.CTkEntry(tab)
        self.psc_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")

        self.insurance_company_label = customtkinter.CTkLabel(tab, text="Insurance Company:")
        self.insurance_company_label.grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.insurance_company_combobox = customtkinter.CTkComboBox(tab,
                                                                    values=[c.name for c in self.insurance_companies])
        self.insurance_company_combobox.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        self.add_person_button = customtkinter.CTkButton(tab, text="Add Person", command=self.add_patient)
        self.add_person_button.grid(row=11, column=0, columnspan=2, pady=10)

    def add_patient(self):
        """
        Adds a new patient.

        Returns
        -------
            None

        Raises
        ------
            ValueError
                If some fields are invalid
        """
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        street = self.street_entry.get()
        house = self.house_entry.get()
        city = self.city_entry.get()
        psc = self.psc_entry.get()
        date_of_birth = self.date_of_birth_entry.get()

        insurance_company_id = next((company.id for company in self.insurance_companies if
                                     company.name == self.insurance_company_combobox.get()), None)
        try:
            patient = Patient(
                id=0,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                phone=phone,
                email=email,
                street=street, house=int(house), city=city, psc=int(psc),
                insurance_company_id=insurance_company_id,
                date_of_birth=datetime.strptime(date_of_birth, "%Y-%m-%d")
            )
            self.app.add_patient_event(patient)

            CTkMessagebox(title="Success", message="Patient added successfully!", icon="info")
            self.withdraw()
        except ValueError as e:
            CTkMessagebox(
                title="Error",
                message=f"Some fields are invalid Make sure to fill all fields correctly! Error message: {e}",
                icon="cancel"
            )
