#Função recursiva
def sobrevivente(soldados, k, indice = 0):
    #Caso base
    if (len(soldados) == 1):
        return soldados[0]
    #Passo recursivo
    indice += k
    if (indice >= len(soldados)):
        indice %= len(soldados)

    soldados.pop(indice)
    return sobrevivente(soldados, k, indice)

#Código principal
soldados = []
n = int(input("Quantos soldados existem? "))
passo = int(input("Com qual passo os soldados se matarão? "))

for i in range(0, n):
    soldados.append(i + 1)

sobrevivente = sobrevivente(soldados, passo)

print(f"O soldado sobrevivente eh o {sobrevivente}.")