import qrcode  as qr
img = qr.make("https://www.youtube.com/@DigitalTyari")
img.save("apptitude_youtube.png")