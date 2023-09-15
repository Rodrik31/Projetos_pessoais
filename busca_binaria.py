def busca_binaria_iterativa(lista, alvo):
    inicio = 0
    fim = len(lista) -1
    
    while inicio <= fim:        
        meio = (inicio + fim) //2
        if alvo == lista[meio]:
            return lista[meio]
        elif alvo > lista[meio]:
            inicio = meio +1
        else:
            fim = meio -1
        print(meio)

    return None    
def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio <= fim:
        meio = (inicio + fim) //2
        print(meio)
        if alvo == lista[meio]:
            return lista[meio]
        elif alvo > lista[meio]:
            return busca_binaria_recursiva(lista, alvo, meio +1, fim)
        else:
            return busca_binaria_recursiva(lista, alvo, inicio, meio -1)
    else:
        return None    


lista = list(range(1,100))
print(busca_binaria_iterativa(lista, 20))
print(busca_binaria_recursiva(lista, 20, 0, len(lista) -1))
