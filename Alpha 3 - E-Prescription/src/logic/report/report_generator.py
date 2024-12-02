from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from datetime import datetime

from src.data.repositories.doctor_repository import DoctorRepo
from src.data.repositories.drug_repository import DrugRepo
from src.data.repositories.patient_repository import PatientRepo
from src.data.repositories.prescription_item_repository import PrescriptionItemRepo
from src.logic.qr.qr_code_generator import QRCodeGenerator
import webbrowser


class ReportGenerator:
    """
    A class used to generate a PDF report for a prescription.

    ...

    Attributes
    ----------
    output_file : str
        the name of the file where the generated report will be saved
    prescription : Prescription
        the prescription for which the report is generated
    db : DatabaseManager
        an instance of the DatabaseManager class which manages the database connection

    Methods
    -------
    __load_data()
        Loads the necessary data for the report from the database.
    generate_pdf(patient: Patient, prescription_items: List[PrescriptionItem], doctor: Doctor)
        Generates a PDF report for the prescription.
    """

    def __init__(self, prescription, db):
        """
        Constructs all the necessary attributes for the ReportGenerator object.

        Parameters
        ----------
            prescription : Prescription
                the prescription for which the report is generated
            db : DatabaseManager
                an instance of the DatabaseManager class which manages the database connection
        """
        self.output_file = f"prescription_{prescription.id}.pdf"
        self.prescription = prescription
        self.db = db
        self.__load_data()
        self.generate_pdf(*self.__load_data())

    def __load_data(self):
        """
        Loads the necessary data for the report from the database.

        Returns
        -------
            Tuple[Patient, List[PrescriptionItem], Doctor]
                a tuple containing the patient, the prescription items, and the doctor
        """
        prescription_items = PrescriptionItemRepo(db=self.db).get_by_prescription(self.prescription)
        doctor = DoctorRepo(db=self.db).get_by_id(self.prescription.issued_by_doctor_id)
        patient = PatientRepo(db=self.db).get_by_id(self.prescription.patient_id)

        return patient, prescription_items, doctor

    def generate_pdf(self, patient, prescription_items, doctor):
        """
        Generates a PDF report for the prescription.

        Parameters
        ----------
            patient : Patient
                the patient for whom the prescription is issued
            prescription_items : List[PrescriptionItem]
                the list of prescription items
            doctor : Doctor
                the doctor who issued the prescription

        Returns
        -------
            None
        """
        # Create a PDF document
        doc = SimpleDocTemplate(self.output_file, pagesize=letter)
        elements = []

        # Define styles
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        attribute_style = ParagraphStyle(
            'AttributeStyle',
            parent=styles['Normal'],
            spaceAfter=6,
        )
        receipt_header = Paragraph("E-Prescription", header_style)
        elements.append(receipt_header)

        QRCodeGenerator.generate_qr_code(self.prescription.id)

        qr_code = Image(QRCodeGenerator.FILE_NAME, width=80, height=80)
        elements.append(qr_code)

        patient_info = [
            ("First Name:", patient.first_name),
            ("Last Name:", patient.last_name),
            ("Date of Birth:", patient.date_of_birth),
            ("Phone:", patient.phone),
            ("Email:", patient.email),
        ]

        elements.append(Paragraph("<b>Patient Information</b>", header_style))
        for attribute, value in patient_info:
            attribute_paragraph = Paragraph(f"- <b>{attribute}</b> {value}", attribute_style)
            elements.append(attribute_paragraph)

        elements.append(Paragraph("<b>Medication</b>", header_style))
        for prescription_item in prescription_items:
            drug = DrugRepo(db=self.db).get_by_id(prescription_item.drug_id)
            medication_info = [
                ("Name:", drug.name),
                ("Dosage:", prescription_item.dosage),
                ("Quantity:", prescription_item.quantity),
                ("Form:", drug.form),
                ("Description:", drug.description),
                ("Side Effects:", drug.side_effects),
                ("Storage Conditions:", drug.storage_conditions),
                ("Instructions:", prescription_item.instructions),
                ("Price:", drug.price),
                ("Picked Up:", "Yes" if prescription_item.picked_up else "No"),
            ]
            for attribute, value in medication_info:
                attribute_paragraph = Paragraph(f"- <b>{attribute}</b> {value}", attribute_style)
                elements.append(attribute_paragraph)

        doctor_info = [
            ("First Name:", doctor.first_name),
            ("Last Name:", doctor.last_name),
            ("Phone:", doctor.phone),
            ("Email:", doctor.email),
        ]

        elements.append(Paragraph("<b>Doctor Information</b>", header_style))
        for attribute, value in doctor_info:
            attribute_paragraph = Paragraph(f"- <b>{attribute}</b> {value}", attribute_style)
            elements.append(attribute_paragraph)

        doc.build(elements)
        webbrowser.open(self.output_file)
