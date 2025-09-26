from googletrans import Translator, LANGUAGES
import asyncio


async def main():
    translator = Translator()

    texto = input('\nQual o texto que quer traduzir: ')
    lingua = str(input('Insira qual lingua para traduzir: '))
    while lingua not in list(LANGUAGES.keys()):
        print('Língua inválida! Tente novamente.')
        lingua = str(input('Insira qual lingua para traduzir: '))

    traduzir_lingua = await translator.translate(texto, dest=lingua)
    print(f'\nTexto Traduzido : {traduzir_lingua.text}')


asyncio.run(main())
