from cv2 import imread
from pathlib import Path
from pyzbar.pyzbar import decode
from os import path, listdir


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_IMAGENS = path.join(BASE_DIR, 'images')
ficheiros = listdir(CAMINHO_IMAGENS)
n = 0
texto = {}

print('\n')
for f in ficheiros:
    n += 1
    if not path.isfile(f):
        pass
    print(f'{n} - {f}')
    texto.update(
        {
            f'{str(n)}': {
                'ficheiro': f
            }
        }
    )

print('\n')
escolha = str(input('Escolha o numero do ficheiro que pretende: '))

while escolha not in texto:
    escolha = str(input('Escolha um numero valido: '))

ficheiro = texto[escolha]['ficheiro']
CAMINHO = path.join(CAMINHO_IMAGENS, ficheiro)

img = imread(CAMINHO)
decoded_objects = decode(img)

for obj in decoded_objects:
    print(f'O texto/site do QRCode é: {obj.data.decode()}')
