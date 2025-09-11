class Node:
    """
    Represents a node in the Binary Search Tree.
    Each node contains a value and optional left/right children.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Implements a Binary Search Tree with insert, search, and inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Searches for a value in the BST.
        Returns True if found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Performs an inorder traversal of the BST.
        Returns a list of values in sorted order.
        """
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

# 🔍 Test Block
bst = BinarySearchTree()
test_values = [50, 30, 70, 20, 40, 60, 80]
for val in test_values:
    bst.insert(val)

print("Inorder Traversal:", bst.inorder_traversal())  

# Search tests
print("Search 60:", bst.search(60))  
print("Search 25:", bst.search(25)) 