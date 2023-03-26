import qrcode
import shutil

texto = str(input('Escreva o site/texto: '))
nome_ficherio = str(input('\nQual sera o nome da foto: '))
formato_imagem = int(input('\nQual sera tipo de imagem: \n1 --> Para ficheiros "png" \n2 --> Para ficheiros "jpeg" \n3 '
                           'Para ficheiros "jpg"\n--> '))

if formato_imagem == 1:
    formato_imagem = "png"
elif formato_imagem == 2:
    formato_imagem = "jpeg"
elif formato_imagem == 3:
    formato_imagem = "jpg"

nome_ficherio_final = nome_ficherio + '.' + formato_imagem
caminho_ficheiro = f'/home/luis/Desktop/Projetos_Python/Desafios-para-Iniciantes-Python/Gerador de QRCode/{nome_ficherio_final}'
caminho_final = '/home/luis/Desktop/Projetos_Python/Desafios-para-Iniciantes-Python/Gerador de QRCode/Fotos/'
img = qrcode.make(texto)
img.save(nome_ficherio_final)

shutil.move(caminho_ficheiro, caminho_final)

print('QRCode guardo')
