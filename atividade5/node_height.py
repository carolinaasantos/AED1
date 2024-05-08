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

    def calculate_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.calculate_height(node.left)
            right_height = self.calculate_height(node.right)
            return max(left_height, right_height) + 1

    def search_node(self, node, target):
        if node is None or node.value == target:
            return node
        elif target < node.value:
            return self.search_node(node.left, target)
        else:
            return self.search_node(node.right, target)
        
    def node_height(self, root, value):
        target_node = self.search_node(root, value)
        if target_node:
            return self.calculate_height(target_node) - 1
        else:
            return 'This node does not belong to the tree.'
    
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
node = int(input(f'Which node do you want to know the height of? Node: '))
height = tree.node_height(tree.root, node)
print(f'The height of the node {node} is {height}')