import qrcode
import sys

def generate_qr():
    data = input("Enter URL or text to generate QR code: ")
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    
    qr.print_ascii()
    print("\nQR Code generated successfully!")

if __name__ == "__main__":
    generate_qr()
