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

# Definição função transfere Stack
def transfStack(a):
    A = Stack()
    for i in range (0, len(a)):
        A.push(a[i])
    return A

# Definição função jogo da pilha
def jogoPilha(a, b, maximo):
    soma = 0
    pontuacao = 0

    while (soma <= maximo):
        if a.size()==0:
            pontuacao += 1 
            soma += b.pop()
        else:
            if b.size()==0:
                pontuacao += 1 
                soma += a.pop()
            else:
                if a.peek() < b.peek():
                    pontuacao += 1 
                    soma += a.pop()
                else:
                    pontuacao += 1
                    soma += b.pop()
        print(soma)
    return pontuacao-1

# Main
a = [5, 2, 9, 4, 6, 3, 1, 2, 4] #topo
b = [2, 6, 9, 7, 2, 5, 1, 4, 2, 5, 3] #topo

a=[6, 4, 3, 2, 1, 1]
b=[5, 2, 3, 4, 2, 1]

A = transfStack(a)
B = transfStack(b)

MAX_SUM = 10

numerosRemovidos = jogoPilha(A, B, MAX_SUM)
print(f"A pontuacao final de Nick eh {numerosRemovidos}")