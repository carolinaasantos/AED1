class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def __str__ (self):
        numbers = []
        node = self.head
        while node is not None:
            numbers.append(node.data)
            node = node.next
        return f'{numbers}'

numbers = [7, 12, 3, 29, 42, 10, 1, 5, 19, 4]
list = LinkedList()

for i in range (0, len(numbers)):
    list.append(numbers[i])

print(f'- Before reversing: {str(list)}')
list.reverse_list()
print(f'- After reversing: {str(list)}')