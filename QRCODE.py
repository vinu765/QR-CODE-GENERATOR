import qrcode

def generatation_of_qr_code(data, filename='qrcode.png'):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=6,
    ) 
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an instance of the QRCodeImage class
    img = qr.make_image(fill_color="brown", back_color="white")
    
    # Save the QR code image to a file
    img.save(filename)

# Example usage
data_that_have_to_encode = "VINU_SWAPNODAYA!"
generatation_of_qr_code(data_that_have_to_encode, 'example_qrcode.png')