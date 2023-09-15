def busca_binaria_iterativa(lista, aposta):
    inicio = 0
    fim = len(lista) -1
    
    while inicio <= fim:        
        meio = (inicio + fim) //2
        if aposta == lista[meio]:
            return lista[meio]
        elif aposta > lista[meio]:
            inicio = meio +1
        else:
            fim = meio -1
        print(meio)

    return None    
def busca_binaria_recursiva(lista, aposta, inicio, fim):
    if inicio <= fim:
        meio = (inicio + fim) //2
        print(meio)
        if aposta == lista[meio]:
            return lista[meio]
        elif aposta > lista[meio]:
            return busca_binaria_recursiva(lista, aposta, meio +1, fim)
        else:
            return busca_binaria_recursiva(lista, aposta, inicio,meio -1)
    else:
        return None    


lista = list(range(1,100))
print(busca_binaria_iterativa(lista, 20))
print(busca_binaria_recursiva(lista, 20, 0, len(lista) -1))
