import qrcode

def create_qr_code(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved as {filename}")

create_qr_code("https://example.com")