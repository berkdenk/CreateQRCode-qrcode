import qrcode

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=25,border=5)

text="www.google.com"
qr.add_data(text)
qr.make(fit=True)

image=qr.make_image(fill_color="black",back_color="white")#qr code color choose
image.save("google.png")