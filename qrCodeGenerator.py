import qrcode

with open ("link.txt", "r") as file:
    file = open("link.txt","r")
for line in file:
    x = line.rstrip()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    imgName = x.split("#/lernkoffer/")[1].replace("/","-") + ".png"
    img.save(imgName)


