from os import path, makedirs
from pathlib import Path
import qrcode


BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_IMAGENS = path.join(BASE_DIR, 'images')
texto = None

if not path.exists(CAMINHO_IMAGENS):
    makedirs(CAMINHO_IMAGENS)

tipo = int(input('''Qual tipo do QRCode:
1> Texto, 
2> Email,
3> Contacto,
4> WIFI
--> '''))


if tipo == 1:
    texto_inicial = ''
    texto_final = ''
    texto = input('Insira o texto: ')
elif tipo == 2:
    texto_inicial = 'mailto: '
    texto_final = ''
    email = input('Insira o email: ')
    texto = f'{texto_inicial}{email}{texto_final}'
elif tipo == 3:
    texto_inicial = 'BEGIN:VCARD'
    texto_final = 'END:VCARD'
    nome = input('Qual nome do usuario: ')
    telefone = input('Qual o telefone do usuario: ')
    email = input('Qual o email do usuario: ')
    texto = f'''
{texto_inicial}
VERSION:3.0
FN:{nome}
TEL:{telefone}
EMAIL:{email}
{texto_final}
'''
elif tipo == 4:
    texto_inicial = 'WIFI:'
    texto_final = ''
    ssid = input('Qual o nome da rede WIFI: ')
    senha = input('Qual a senha da rede WIFI: ')
    tipo_seguranca = input('Qual o tipo de seguranca (WEP/WPA/nulo): ')
    texto = f'{texto_inicial}T:{tipo_seguranca};S:{ssid};P:{senha};;{texto_final}'

nome_ficheiro = str(input('Qual o nome do ficheiro nulo para padrao: '))
tipo_imagem = str(input('''Qual o tipo do formato da imagem:
> png
> jpeg
> jpg
--> ''')).lower()

if tipo_imagem not in ['png', 'jpeg', 'jpg']:
    print('Formato invalido, sera usado png por defeito.')
    tipo_imagem = 'png'


img = qrcode.make(texto)
img.save(path.join(CAMINHO_IMAGENS, f'{nome_ficheiro}.{tipo_imagem}'))
print(f'QRCode gerado com sucesso em {path.join(CAMINHO_IMAGENS, f'{nome_ficheiro}.{tipo_imagem}')}')
