from tkinter import Scale
# import png
from pyqrcode import QRCode

s = '202130004'
url = pyqrcode.create(s)
url.png('MeuQRCode.png',scale=6)