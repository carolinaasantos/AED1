class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_left(node, value):
    if node is not None:
        node.left = Node(value)
    else:
        print("Error: The provided node is None.")

def insert_right(node, value):
    if node is not None:
        node.right = Node(value)
    else:
        print("Error: The provided node is None.")

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

def sum_inner_nodes(node):
    if node:
        if node.left is not None or node.right is not None:
            return node.value + sum_inner_nodes(node.left) + sum_inner_nodes(node.right)
        else:
            return 0
    else:
        return 0

root = Node(11)

insert_left(root, 24)
insert_right(root, 30)
insert_left(root.left, 40)
insert_right(root.left, 26)
insert_left(root.right, 48)
insert_right(root.right, 58)
insert_left(root.left.left, 42)
insert_right(root.left.left, 46)

print("Preorder: ", end="")
preorder(root)
print("\nInorder: ", end="")
inorder(root)
print("\nPostorder: ", end="")
postorder(root)