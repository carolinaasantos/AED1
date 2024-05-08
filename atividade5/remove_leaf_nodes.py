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

    def removeLeafNodes(self, root):
        if root is not None:
            if root.left is None and root.right is None:
                return None
            else:
                root.left = self.removeLeafNodes(root.left)
                root.right = self.removeLeafNodes(root.right)
        return root
    
tree_root = Node(70)
tree = Binary_tree(tree_root)

tree.insert(tree_root, 31)
tree.insert(tree_root, 93)
tree.insert(tree_root.left, 14)
tree.insert(tree_root.right, 73)
tree.insert(tree_root.right, 94)
tree.insert(tree_root.left.left, 23)

print(f'=== Using preorder sequence to show all the nodes of the tree ===')
print(f'Binary tree before removing leaf nodes:')
tree.preorder(tree.root)
print('')
print(f'Binary tree after removing leaf nodes:')
tree.removeLeafNodes(tree.root)
tree.preorder(tree.root)