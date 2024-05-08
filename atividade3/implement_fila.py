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
    
# Definição classe Fila
class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        while self.stack1.size() != 0:
            self.stack2.push(self.stack1.pop())
        self.stack1.push(item)
        while self.stack2.size() != 0:
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        if self.stack1.size() == 0:
            raise Exception("Cannot pop from empty queue")
        return self.stack1.pop()
    

    def peek(self):
        if self.stack1.size() == 0:
            raise Exception("Cannot peek from empty queue")
        else:
            return self.stack1.peek()
    
    def size(self):
        return self.stack1.size()

# Main
fila = Queue()
for i in range (1, 6):
    fila.enqueue(i)

print(f"O primeiro elemento da fila eh {fila.peek()}")

fila.dequeue()

print(f"Mas retirando-o da fila, obtemos:")

for i in range(0, fila.size()):
    print(fila.dequeue(), end=' ')