def bubblesort(array):
    for i in range (len(array) - 1, 0, -1):
        for j in range (0, len(array) - 1):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
        print(array)
    return array

numeros = [77, 1, 6, 29, 91, 86, 92, 93, 89, 10, 36, 46, 60, 50, 53]
print("")
numeros = bubblesort(numeros)
print("")
print("O vetor ordenado é: ")
print(numeros)
print("")

