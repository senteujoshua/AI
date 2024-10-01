class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, root, key):
        if root is None:
            return root

        # Traverse the tree
        if key < root.key:
            root.left = self._delete_node(root.left, key)
        elif key > root.key:
            root.right = self._delete_node(root.right, key)
        else:
            # Node to be deleted found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: get inorder successor
            min_larger_node = self._min_value_node(root.right)
            root.key = min_larger_node.key
            root.right = self._delete_node(root.right, min_larger_node.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

# Create BST and perform operations
bst = BinarySearchTree()

# 1. Insert values: 50, 30, 70, 20, 40, 60, 80
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for value in values_to_insert:
    bst.insert(value)
    print(f"Inserting {value}...")
    bst.print_tree(bst.root)
    print("In-order Traversal:", bst.in_order_traversal())
    print("-" * 30)

# 2. Delete value 70
print("Deleting 70...")
bst.delete(70)
bst.print_tree(bst.root)
print("In-order Traversal:", bst.in_order_traversal())
print("-" * 30)

# 3. Search for value 20
search_key = 20
found_node = bst.search(search_key)
if found_node:
    print(f"Value {search_key} found in the tree.")
else:
    print(f"Value {search_key} not found in the tree.")
bst.print_tree(bst.root)
print("In-order Traversal:", bst.in_order_traversal())
