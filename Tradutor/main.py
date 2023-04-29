from googletrans import Translator
import json

with open("Linguas.json", "r") as dt:
    data = json.load(dt)

translator = Translator()
lingua = str(input('Insira qual lingua do texto: '))
traduzir_lingua = translator.translate(lingua, dest='en').text
print(traduzir_lingua)

'''texto = str(input('Insira o que quer traduzir: '))
translated_text = translator.translate(texto, src=f'{traduzir_lingua}', dest='pt').text
print(translated_text)'''

