import cv2
from pyzbar.pyzbar import decode

caminho = str(input('Insira o caminho da foto: '))
img = cv2.imread(caminho)
decoded_objects = decode(img)

for obj in decoded_objects:
    print(f'O texto/site do QRCode é {obj.data.decode()}')
