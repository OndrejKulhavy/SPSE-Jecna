# Analysis

The Healthcare E-Prescription App is a Python-based application designed to streamline the generation and management of
electronic prescriptions within the framework of the Czech Architecture of eGovernment. Drawing inspiration from modules
such as
`A1243 Lečiva`, `A1341 Zdravotní pojištění`, `A3726 eRecept`, and `A4006 Národní registr zdravotních pracovníků`, this
app is a school project for the subject `Programové vybavení` at
the [Secondary technical school of electrical engineering Ječná](https://www.spsejecna.cz/) in Prague.

## Requirements

This app has to fulfill [these requirements](Requirements.md) given by the school.

## Architecture

The app is built upon a 3-tier architecture, providing a structured and modular design for optimal performance and
scalability.

1. **User Interface `Presentation Layer`**
    - Utilize the [customTkinter](https://github.com/TomSchimansky/CustomTkinter) library for a user-friendly and
      customized graphical interface.
    - The GUI is designed using [Figma](https://www.figma.com/), a collaborative UI/UX design tool.

2. **Logic Layer**
    - Created in Python `3.12`, this layer handles the main operations of the application, making sure different parts
      work smoothly together.
    - The [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) library is used to connect to the
      database.
    - For working with images, the app relies on the [Pillow](https://pypi.org/project/Pillow/) library.
    - Managing environment variables is made easy with the [python-dotenv](https://pypi.org/project/python-dotenv/)
      library.
    - Generating PDF files is done using the [ReportLab](https://pypi.org/project/reportlab/) library.
    - Generating QR codes is handled by [qrcode](https://pypi.org/project/qrcode/) library.

3. **Data Layer**
    - MySQL is employed as the database management system to handle the storage and retrieval of healthcare data
      securely.

## Database

