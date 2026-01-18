import qrcode

while True:
    data = input("Masukkan teks atau URL: ").strip()
    if not data:
        print("Data tidak boleh kosong!")
        continue
    
    filename = input("Masukkan nama file (contoh: qrcode.png): ").strip()
    if not filename:
        filename = "qrcode.png"
    
    try:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        image = qr.make_image(fill_color="black", back_color="white")
        image.save(filename)
        print(f"Kode QR berhasil disimpan sebagai {filename}")
    except Exception as e:
        print(f"Error: {e}")
    
    again = input("\nBuat QR code lagi? (y/n): ").lower()
    if again != 'y':
        print("Terima kasih!")
        break

