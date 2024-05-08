def insertionsort(array):
    for i in range (1, len(array)):
        j = i
        while (j > 0) and (array[j] < array[j-1]):
            aux = array[j]
            array[j] = array[j-1]
            array[j-1] = aux
            j -= 1
            print(array)
    return array

numeros = [77, 1, 6, 29, 91, 86, 92, 93, 89, 10, 36, 46, 60, 50, 53]
print("")
numeros = insertionsort(numeros)
print("O vetor ordenado é: ")
print(numeros)
print("")


