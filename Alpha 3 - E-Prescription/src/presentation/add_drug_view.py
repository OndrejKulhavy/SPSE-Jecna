import customtkinter
from CTkMessagebox import CTkMessagebox

from src.data.models.drug import Drug


class AddDrugView(customtkinter.CTkToplevel):
    """
    A class used to manage the Add Drug view.

    ...

    Attributes
    ----------
    app : App
        an instance of the App class which manages the application
    forms : List[DrugForm]
        a list of drug forms

    Methods
    -------
    __add_second_tab(tabview: customtkinter.CTkTabview)
        Adds the second tab to the tab view.
    __add_first_tab(tabview: customtkinter.CTkTabview)
        Adds the first tab to the tab view.
    add_medication()
        Adds a new medication.
    """

    TAB1 = "Manually"
    TAB2 = "From File"

    def __init__(self, app, forms):
        """
        Constructs all the necessary attributes for the AddDrugView object.

        Parameters
        ----------
            app : App
                an instance of the App class which manages the application
            forms : List[DrugForm]
                a list of drug forms
        """
        super().__init__()
        self.resizable(False, False)
        self.title("Add drug")
        self.app = app
        self.forms = forms

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
                                                 text="You can add multiple medications at once by uploading a csv file.")
        self.text_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="w")

        self.file_label = customtkinter.CTkLabel(tab, text="File:")
        self.file_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.file_entry = customtkinter.CTkEntry(tab)
        self.file_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.browse_button = customtkinter.CTkButton(tab, text="Browse")
        self.browse_button.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.add_medication_button_file = customtkinter.CTkButton(tab, text="Add Medication")
        self.add_medication_button_file.grid(row=5, column=3, columnspan=2, pady=30)

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
        self.name_label = customtkinter.CTkLabel(tab, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = customtkinter.CTkEntry(tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.price_label = customtkinter.CTkLabel(tab, text="Price:")
        self.price_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.price_entry = customtkinter.CTkEntry(tab)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.active_substance_label = customtkinter.CTkLabel(tab, text="Active Substance:")
        self.active_substance_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.active_substance_entry = customtkinter.CTkEntry(tab)
        self.active_substance_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.form_label = customtkinter.CTkLabel(tab, text="Form:")
        self.form_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.form_combobox = customtkinter.CTkComboBox(tab, values=[form.name for form in self.forms])
        self.form_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.description_label = customtkinter.CTkLabel(tab, text="Description:")
        self.description_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.description_entry = customtkinter.CTkEntry(tab)
        self.description_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.side_effects_label = customtkinter.CTkLabel(tab, text="Side Effects:")
        self.side_effects_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.side_effects_entry = customtkinter.CTkEntry(tab)
        self.side_effects_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.storage_conditions_label = customtkinter.CTkLabel(tab, text="Storage Conditions:")
        self.storage_conditions_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.storage_conditions_entry = customtkinter.CTkEntry(tab)
        self.storage_conditions_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.add_medication_button = customtkinter.CTkButton(tab, text="Add Medication", command=self.add_medication)
        self.add_medication_button.grid(row=10, column=0, columnspan=2, pady=10)

    def add_medication(self):
        """
        Adds a new medication.

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
            name = self.name_entry.get()
            price = self.price_entry.get()
            active_substance = self.active_substance_entry.get()
            form_id = next((form.id for form in self.forms if form.name == self.form_combobox.get()), None)
            description = self.description_entry.get()
            side_effects = self.side_effects_entry.get()
            storage_conditions = self.storage_conditions_entry.get()

            drug = Drug(
                id=0,
                name=name,
                price=float(price),
                active_substance=active_substance,
                form=form_id,
                description=description,
                side_effects=side_effects,
                storage_conditions=storage_conditions
            )

            self.app.add_drug_event(drug)

            CTkMessagebox(title="Success", message="Drug added successfully!", icon="info")
            self.withdraw()

        except ValueError as e:
            CTkMessagebox(title="Error",
                          message=f"Some fields are invalid Make sure to fill all fields correctly! Error message: {e}",
                          icon="cancel")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"An unexpected error occurred: {e}", icon="cancel")