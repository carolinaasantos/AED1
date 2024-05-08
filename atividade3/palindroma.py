# Definição classe Pilha
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def peek(self):
        return self.items[-1]
    
    def push(self, chave):
        self.items.append(chave)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# Definição função que verifica se uma palavra é palíndroma
def ehPalindroma(palavra):
    a = Stack()
    b = Stack()
    copia = Stack()

    for i in range (0, len(palavra)):
        a.push(palavra[i])
        copia.push(palavra[i])

    tamanho = a.size()

    for i in range (0, tamanho):
        b.push(copia.pop())

    palindroma = True

    for i in range (0, tamanho):
        if a.pop() != b.pop():
            palindroma = False
            return palindroma
    return palindroma

def resposta(palavra, verifica):
    if (verifica):
        print(f'A palavra "{palavra}" eh palindroma')
    else:
        print(f'A palavra "{palavra}" nao eh palindroma')

# Main
palavra1 = "carolina"
palavra2 = "arara"
palavra3 = "alexandre"
palavra4 = "rodador"

resposta(palavra1, ehPalindroma(palavra1))
resposta(palavra2, ehPalindroma(palavra2))
resposta(palavra3, ehPalindroma(palavra3))
resposta(palavra4, ehPalindroma(palavra4))
