import qrcode

with open ("link.txt", "r") as file:
    file = open("link.txt","r")
for line in file:
    x = line.rstrip()
    img = qrcode.make(x)
    imgName = x.split("#/lernkoffer/")[1].replace("/","-") + ".png"
    img.save(imgName)

file.close()
    