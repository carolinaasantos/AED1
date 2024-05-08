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

# Main
n = 24
i = 2
fatores = Stack()
while (n > 1):
    if n % i == 0:
        fatores.push(i)
        n /= i
    else:
        if i > 2:
            i += 2
        else:
            i += 1

while (fatores.size() != 0):
    print(fatores.pop(), end=' ')