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

    def add_ordered_list(self, other_list):
        key = other_list.head
        for i in range (0, other_list.size):
            temp = self.head
            previous = None
            print(f'Data: {key.data}')
            while temp is not None and type(temp.data) is int:
                if int(temp.data) > int(key.data):
                    break
                else:
                    previous = temp
                    temp = temp.next
            number = Node(key)
            if previous is None:
                number.next = self.head
                self.head = number
            else:
                number.next = temp
                previous.next = number
            key = key.next
            if key is None:
                break
        return self

    def __str__ (self):
        numeros = []
        node = self.head
        while node is not None:
            numeros.append(node.data)
            node = node.next
        return f'{numeros}'

    def add_numbers(self, list_of_numbers):
        for i in range (0, len(list_of_numbers)):
            self.append(list_of_numbers[i])

def add_lists(list1, list2):

    new_list = LinkedList()
    node1 = list1.head
    node2 = list2.head

    while node1 is not None and node2 is not None:
        if node1.data < node2.data:
            new_list.append(node1.data)
            node1 = node1.next
        else:
            new_list.append(node2.data)
            node2 = node2.next
    while node1 is not None:
        new_list.append(node1.data)
        node1 = node1.next
    while node2 is not None:
        new_list.append(node2.data)
        node2 = node2.next

    return new_list

l1 = [5, 12, 19, 23, 29, 42]
l2 = [2, 3, 7, 15, 20, 25, 33, 39]

list1 = LinkedList()
list2 = LinkedList()

list1.add_numbers(l1)
list2.add_numbers(l2)

final_ordered_list = add_lists(list1, list2)

print(f'Merged list: {final_ordered_list}')