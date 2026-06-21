import qrcode

data=input('enter any text or URL: ').strip()
filename=input('enter filename: ').strip()

qr=qrcode.QRCode(box_size=12,border=5)
qr.add_data(data)

image=qr.make_image(fill_colour='black',back_colour='white')

image.save(filename)

