import qrcode


class QRCodeGenerator:
    """
    A class used to generate QR codes.

    ...

    Attributes
    ----------
    FILE_NAME : str
        the name of the file where the generated QR code will be saved

    Methods
    -------
    generate_qr_code(data: str)
        Generates a QR code from the provided data and saves it as an image.
    """

    FILE_NAME = "qr_code.png"

    @staticmethod
    def generate_qr_code(data: str):
        """
        Generates a QR code from the provided data and saves it as an image.

        Parameters
        ----------
            data : str
                the data to be encoded into the QR code

        Returns
        -------
            None
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(QRCodeGenerator.FILE_NAME)
