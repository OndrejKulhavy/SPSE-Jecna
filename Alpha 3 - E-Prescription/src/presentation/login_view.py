import customtkinter
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox


class LoginView(customtkinter.CTk):
    """
    A class used to manage the Login view.

    ...

    Attributes
    ----------
    app : App
        an instance of the App class which manages the application

    Methods
    -------
    __init__(app: App)
        Constructs all the necessary attributes for the LoginView object.
    create_widgets()
        Creates the widgets for the view.
    login()
        Handles the login event.
    """

    WINDOW_SIZE = "230x320"

    def __init__(self, app):
        """
        Constructs all the necessary attributes for the LoginView object.

        Parameters
        ----------
            app : App
                an instance of the App class which manages the application
        """
        super().__init__()
        self.title("Login")
        customtkinter.set_default_color_theme("green")
        self.geometry(self.WINDOW_SIZE)
        self.resizable(False, False)
        self.create_widgets()
        self.app = app

    def create_widgets(self):
        """
        Creates the widgets for the view.

        Returns
        -------
            None
        """
        # Add a label for the image
        self.image_label = customtkinter.CTkLabel(self)
        self.image_label.pack()

        # Create other widgets
        self.label_username = customtkinter.CTkLabel(self, text="Email")
        self.label_username.pack()

        self.entry_username = customtkinter.CTkEntry(self, placeholder_text="Enter your email")
        self.entry_username.pack(pady=5)  # Add some padding between the label and entry widgets

        self.label_password = customtkinter.CTkLabel(self, text="Password")
        self.label_password.pack()

        self.entry_password = customtkinter.CTkEntry(self, show="*", placeholder_text="Enter your password")
        self.entry_password.pack(pady=5)  # Add some padding between the label and entry widgets

        self.button_login = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.button_login.pack(pady=25)  # Add more padding below the button for separation

        # Load the image and set it as the label's image
        image = customtkinter.CTkImage(Image.open("./resources/social_preview_wbg.png"), size=(238, 116))
        self.image_label.configure(image=image, text="")
        self.image_label.image = image

        # Center the image label on top of the window
        self.image_label.pack(side="top", fill="both", expand=True, anchor="center")

    def login(self):
        """
        Handles the login event.

        Returns
        -------
            None

        Raises
        ------
            ValueError
                If the username or password is invalid
        """
        try:
            self.app.login_event(self.entry_username.get(), self.entry_password.get())
            self.withdraw()
        except ValueError as e:
            CTkMessagebox(title="Error", message=str(e), icon="cancel")
