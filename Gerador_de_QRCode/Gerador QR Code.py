from os import path
from os import makedirs
from os import rmdir
import qrcode


if path.exists('Gerador_de_QRCode/Fotos'):
    rmdir('Gerador_de_QRCode/Fotos')
if not path.exists('Gerador_de_QRCode/Fotos'):
    makedirs('Gerador_de_QRCode/Fotos')

TEXTO = str(input('Escreva a mensagem do QRCode: '))
NOME_FICHEIRO = str(input('\nQual sera o nome da foto: '))
formato_imagem = int(input('''\nQual sera tipo de imagem:
1 --> Para ficheiros "png"
2 --> Para ficheiros "jpeg" 
3 --> Para ficheiros "jpg"
-> '''))

if formato_imagem == 1:
    FORMATO_IMAGEM_FINAL = ".png"
elif formato_imagem == 2:
    FORMATO_IMAGEM_FINAL = ".jpeg"
elif formato_imagem == 3:
    FORMATO_IMAGEM_FINAL = ".jpg"

NOME_FICHEIRO_FINAL = NOME_FICHEIRO + FORMATO_IMAGEM_FINAL
img = qrcode.make(TEXTO)
img.save(f'Gerador_de_QRCode/Fotos/{NOME_FICHEIRO_FINAL}')
