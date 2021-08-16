def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = int(lista[meio])
        if chute == item:
            return meio 
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    raise Exception("Item indisponível na lista!")


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

item = int(input("Digite o item: "))
print("Resultado: ",pesquisa_binaria(minha_lista, item))