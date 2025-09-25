from os import path
from os import makedirs
from string import ascii_letters, digits
from pathlib import Path
from random import sample
from uuid import uuid4
import qrcode


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_IMAGENS = path.join(BASE_DIR, 'images')
SIMBOLOS = '!#$%&()*+,-./:;<=>?@[]^_{|}~'
JUNCAO = ascii_letters + digits + SIMBOLOS
QUANTCATR = 0
QUANTIDADE_PASSWORDS = 0
N = 0

if not path.exists(CAMINHO_IMAGENS):
    makedirs(CAMINHO_IMAGENS)

QUANTCATR = int(input('Quantos caracteres quer na password? (min 6, max 50): '))
if QUANTCATR < 6 or QUANTCATR > 50:
    print('O numero de caracteres nao pode ser menor que 6 e maior que 50')
    print('A usar valor padrao de 15')
    QUANTCATR = 15

QUANTIDADE_PASSWORDS = int(input('Quantas passwords quer gerar? '))
if QUANTIDADE_PASSWORDS > 1 or QUANTIDADE_PASSWORDS > 30:
    print('O numero de passwords nao pode ser menor que 1 e maior que 30')
    print('A usar valor padrao de 5')
    QUANTIDADE_PASSWORDS = 5

while N < QUANTIDADE_PASSWORDS:
    N += 1
    id_password = str(uuid4()).replace('-', '')[:7]
    password = ''.join(sample(JUNCAO, QUANTCATR))
    print(f'Password: {password}')

    exportacao = input('Quer exportar a password para um QRCode? (s/n) ').lower()
    if exportacao == 's':
        NOME_FICHEIRO = f'Password_{str(id_password)}.png'
        image = qrcode.make(password)
        image.save(path.join(CAMINHO_IMAGENS, NOME_FICHEIRO))
        print(f'Password exportada com sucesso para {path.join(CAMINHO_IMAGENS, NOME_FICHEIRO)}')
    else:
        continue
