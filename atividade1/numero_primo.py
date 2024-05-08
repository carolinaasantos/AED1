import math

#Função recursiva
def isPrime(n, i):
    #Caso base
    if(i >= math.sqrt(n)):
        return True
    elif(i > 1 and n % i == 0):
        return False
    #Passo recursivo
    else:
        return isPrime(n, i+1)

#Código principal
numero = 12
print(isPrime(numero, 1))