import qrcode, os

link_texto = str(input('Insira o site/texto que quer: '))
print('Site/texto gravado \n')
nome_ficheiro = str(input('Insira o nome do arquivo: '))
print('Nome do arquivo gravado \n')
tipo_imagem = int(input('Insira  qual tipo de imagem: \n1 --> Para ficheiros "png" \n2 --> Para ficheiros "jpeg" \n3 --> Para ficheiros "jpg"\n--> '))
print('Tipo de imagem gravado')

formato_imagem = ""
if tipo_imagem == 1:
    formato_imagem = "png"
elif tipo_imagem == 2:
    formato_imagem = "jpeg"
elif tipo_imagem == 3:
    formato_imagem = "jpg"

print('\nA gerar seu QR Code')
img = qrcode.make(link_texto)
print('Qr Code gerado, gravando na pasta')
ficheiros = os.path.idfir("/luisgomes/imagens/Qr Code")
if ficheiros == True:
    img.save(f"{nome_ficheiro}.{formato_imagem}")
elif ficheiros == False:
    os.makedir('.imagens/Qr Code')
    img.save(f"{nome_ficheiro}.{formato_imagem}")
print('Qr Code guardado em seu pc')
print('Obrigado por usar')