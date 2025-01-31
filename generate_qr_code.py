import qrcode

# Data to be encoded
data = "https://ar-frame.vercel.app/sam.mp4"  # Replace with the data you want to encode in the QR code

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR Code as an image file
img.save("your_qr_code.png")
