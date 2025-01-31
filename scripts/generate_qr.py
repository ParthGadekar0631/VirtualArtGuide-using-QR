import qrcode
from PIL import Image

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == '__main__':
    sample_data = "https://www.example.com"
    output_file = "app/static/qr_codes/portrait1_qr.png"
    generate_qr_code(sample_data, output_file)