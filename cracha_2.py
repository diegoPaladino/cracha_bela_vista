
# Fonts: 
# https://nsworld.com.br/como-gerar-facilmente-qrcode-com-python/
# https://www.gustahtocantins.com.br/2020/09/como-criar-um-qr-code-em-python.html

# # import pypng
# from pyqrcode import QRCode
# s = "202130004"
# url = pyqrcode.create(s)
# # url.png("MeuQRCode.png",scale=6)


# url = pyqrcode.create(s)


import pyqrcode
from pyqrcode import QRCode

s = " 202130004\n\n MANOEL MAKAULLE DOS SANTOS DA SILVA\n\n EF401VA21\n\n TESTANDO TEXTO AINDA MAIOR"

url = pyqrcode.create(s)

url.svg(".svg", scale = 8)