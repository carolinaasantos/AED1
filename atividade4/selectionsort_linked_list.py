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

    def selection_sort(self):
        current = self.head
        while current:
            lower_node = current
            temp = current.next
            while temp:
                if temp.data < lower_node.data:
                    lower_node = temp
                temp = temp.next
            temp = current.data
            current.data = lower_node.data
            lower_node.data = temp
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return f'{result}'

    def add_numbers(self, list_of_numbers):
        for i in range (0, len(list_of_numbers)):
            self.append(list_of_numbers[i])

numbers = [6, 11, 2, 28, 41, 9, 0, 4, 18, 3]
list = LinkedList()

list.add_numbers(numbers)

print(f'- Before ordering: {str(list)}')
list.selection_sort()
print(f'- After ordering: {str(list)}')