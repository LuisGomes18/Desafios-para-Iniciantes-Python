from cv2 import imread
from pyzbar.pyzbar import decode


caminho = str(input('Insira o caminho da foto: '))
img = imread(caminho)
decoded_objects = decode(img)

for obj in decoded_objects:
    print(f'O texto/site do QRCode é {obj.data.decode()}')
