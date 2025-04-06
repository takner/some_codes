#python -m venv .venv
#.venv\Scripts\activate
#pip install Pillow
#pip install qrcode

import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data('https://etehadgroup.co/links')
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")

qr_image.save('etehadgroup-card.png')