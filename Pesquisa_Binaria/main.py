def pesquisa_binaria(vet: list, chave: int, tamanho: int):
    inf = 0
    superior = tamanho - 1

    while inf <= superior:
        meio = (inf + superior) // 2
        if chave == vet[meio]:
            return meio
        if chave > vet[meio]:
            inf = meio + 1
        else:
            superior = meio - 1

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = pesquisa_binaria(array, 7, len(array))
print(resultado)
