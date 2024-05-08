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

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Definição classe Fila
class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue')
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def size(self):
        return self._size

# Main
estudantes = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
sanduiches = [0, 0, 0, 0, 1, 0, 1, 1, 0, 1]

alunos = Queue()
for i in range (0, len(estudantes)):
    alunos.enqueue(estudantes[i])

lanches = Stack()
for i in range (len(sanduiches) - 1, -1, -1):
    lanches.push(sanduiches[i])

alguemCome = True
foiProFinal = 0

while alunos.size() != 0 and alguemCome:
    if alunos.front.data == lanches.peek():
        alunos.dequeue()
        lanches.pop()

    else:
        if alunos.front.data != lanches.peek():
            alunos.enqueue(alunos.dequeue())
            foiProFinal += 1

            if foiProFinal > lanches.size():
                alguemCome = False

print(f'O numero de alunos que nao comeu foi {lanches.size()}')
