#Função recursiva para encontrar o maior elemento
def maiorElemento(vetor, qntdElem):
    if (qntdElem == 1):
        return vetor[0]
    else:
        maior = maiorElemento(vetor, qntdElem-1)
        if (maior > vetor[qntdElem-1]):
            return maior
        else:
            return vetor[qntdElem-1]

#Declaração do array
array = [9, 10, 2, 1, 5, 6, 7, 4, 15, 20, 8, 3]

#Chamada da função para encontrar o maior elemento
maiorElem = maiorElemento(array, len(array))

#Resposta
print (f'O maior elemento eh {maiorElem}')