import cv2
from pyzbar.pyzbar import decode

# carrega a imagem do QR Code
img = cv2.imread('qr_code.png')

# decodifica o QR Code
decoded_objects = decode(img)

# imprime o texto contido no QR Code
for obj in decoded_objects:
    print(obj.data.decode())
