class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self, root):
        self.root = root

    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.value:
            node.left = self.insert(node.left, key)
        elif key > node.value:
            node.right = self.insert(node.right, key)
        return node

    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def calculate_depth(self, node, target, depth):
        if node is None:
            return -1
        elif node.value == target:
            return depth
        elif target < node.value:
            return self.calculate_depth(node.left, target, depth + 1)
        else:
            return self.calculate_depth(node.right, target, depth + 1)
        
    def node_depth(self, root, value):
        return self.calculate_depth(root, value, 0)
    
tree_root = Node(70)
tree = Binary_tree(tree_root)

tree.insert(tree_root, 31)
tree.insert(tree_root, 93)
tree.insert(tree_root.left, 14)
tree.insert(tree_root.right, 73)
tree.insert(tree_root.right, 94)
tree.insert(tree_root.left.left, 23)

print(f'=== Using preorder sequence to show all the nodes of the tree ===')
print(f'Binary search tree: ', end='')
tree.preorder(tree.root)
print('')
node = int(input(f'Which node do you want to know the depth of? Node: '))
depth = tree.node_depth(tree.root, node)
print(f'The height of the node {node} is {depth}')