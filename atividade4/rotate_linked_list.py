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
        self.size += 1

    def rotate_position(self, k):
        if self.head is None or k <= 0:
            return
        k = k % self.size
        if k == 0:
            return
        current = self.head
        for i in range (0, self.size - k - 1):
            current = current.next
        new_head = current.next
        current.next = None
        current = new_head
        while current.next:
            current = current.next
        current.next = self.head
        self.head = new_head

    def add_numbers(self, list_of_numbers):
        for i in range (0, len(list_of_numbers)):
            self.append(list_of_numbers[i])

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return f'{result}'

numbers = [1, 3, 4, 7, 9]
list = LinkedList()

list.add_numbers(numbers)

print(f'List without rotation: {str(list)}')

list.rotate_position(1)
print(f'List with rotation of {1} position: {str(list)}')

list.rotate_position(1)
print(f'List with rotation of {2} positions: {str(list)}')

list.rotate_position(1)
print(f'List with rotation of {3} positions: {str(list)}')