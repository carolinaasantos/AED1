def selectionsort(array):
    for i in range (0, len(array)):
        menor = i
        for j in range (i+1, len(array)):
            if (array[j] < array[menor]):
                menor = j
        aux = array[i]
        array[i] = array[menor]
        array[menor] = aux
        print(array)
    return array

numeros = [77, 1, 6, 29, 91, 86, 92, 93, 89, 10, 36, 46, 60, 50, 53]
numeros = selectionsort(numeros)
print("O vetor ordenado é: ")
print(numeros)


