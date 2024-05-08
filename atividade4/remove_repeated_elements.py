class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, key):
        tail = Node(key)
        if self.head is None:
            self.head = tail
            tail.prev = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = tail
            tail.prev = temp
        tail.next = None
        self.size += 1

    def remove_repeated_numbers(self):
        current = self.head
        while current:
            next_one = current.next
            while next_one:
                if current.data == next_one.data:
                    next_one.prev.next = next_one.next
                    if next_one.next:
                        next_one.next.prev = next_one.prev
                    self.size -= 1
                next_one = next_one.next
            current = current.next

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

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5]
list = DoubleLinkedList()

list.add_numbers(numbers)

print(f'List without removing repeated numbers: {str(list)}')
list.remove_repeated_numbers()
print(f'List after removing repeated numbers: {str(list)}')
