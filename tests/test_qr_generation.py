import os
import qrcode
from scripts.generate_qr import generate_qr

def test_generate_qr():
    """
    Test that the QR code is generated correctly and saved as a file.
    """
    # Test data
    sample_data = "https://example.com/portrait/1"
    output_file = "app/static/qr_codes/test_qr.png"

    # Generate QR code
    generate_qr(sample_data, output_file)

    # Check if the file is created
    assert os.path.exists(output_file), "QR code file was not created."

    # Cleanup
    os.remove(output_file)
