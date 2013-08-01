from fifo_queue import Queue
from stack import Stack


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.children = []

    def __str__(self):
        return '(%s, %s, %s)' % (self.key, self.value,
                                 ','.join([str(_) for _ in self.children]))


class Tree:
    @staticmethod
    def from_list(xs):
        def node_from_list(l):
            node = Node(l[0], l[1])
            node.children = [node_from_list(_) for _ in l[2]]
            return node
        tree = Tree()
        tree.root = node_from_list(xs)
        return tree

    def __init__(self):
        self.root = Node()

    def __str__(self):
        return str(self.root)

    def insert(self, key, value):
        pass

    def height(self):
        def _height(node):
            if not node.children:
                return 1
            else:
                return 1 + max(_height(_) for _ in node.children)
        return _height(self.root)

    def dfs(self, key):
        """Depth-first search for a given key. O(|nodes|)
        Pros:
            - much lower memory requirements
            - works well if the key is likely found on one of the
              deeper levels in the tree (e.g. a leaf node)
        Cons:
            - works badly if the key is likely found on one of the
              upper levels in the tree
        """
        nodes = Stack()
        nodes.push(self.root)
        while not nodes.is_empty:
            node = nodes.pop()
            if node.key == key:
                return node.value
            else:
                for child in node.children:
                    nodes.push(child)

    def dfs_recursive(self, node, key):
        if node.key == key:
            return node.value
        for child in node.children:
            found_value = self.dfs_recursive(child, key)
            if found_value is not None:
                return found_value
        return None

    def bfs(self, key):
        """Breadth-first search for a given key. O(|nodes|)
        Pros:
            - works well if the key is likely found on one of the
              upper levels in the tree
        Cons:
            - much higher memory requirements
            - works badly if the key is likely found on one of the
              deeper levels in the tree (e.g. if we're looking for
              a leaf node)
        """
        nodes = Queue()
        nodes.enqueue(self.root)
        while not nodes.is_empty:
            node = nodes.dequeue()
            if node.key == key:
                return node.value
            else:
                for child in node.children:
                    nodes.enqueue(child)


class BinaryNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return '(%s, %s, %s, %s)' % (self.key, self.value,
                                     self.left, self.right)


class BinarySearchTree:
    def __init__(self):
        self.root = BinaryNode()

    def __str__(self):
        return str(self.root)

    def insert(self, key, value):
        node = self.root
        while node:
            if node.key is None:
                node.key = key
                node.value = value
                return
            if key == node.key:
                node.value = value
                return
            if key < node.key:
                if node.left is None:
                    node.left = BinaryNode(key, value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = BinaryNode(key, value)
                    return
                node = node.right

    def find(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def find_recursive(self, node, key):
        if node.key == key:
            return node.value
        elif key < node.key:
            return self.find_recursive(node.left, key)
        else:
            return self.find_recursive(node.right, key)

    def min(self):
        node = self.root
        while node:
            if node.left is None:
                return node.key
            node = node.left

    def max(self):
        node = self.root
        while node:
            if node.right is None:
                return node.key
            node = node.right

    def height(self):
        def _height(node):
            if node is None:
                return 0
            else:
                return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def traverse_preorder(self, node=None):
        if node is None:
            node = self.root
        visited = [node.key]
        if node.left:
            visited += self.traverse_preorder(node.left)
        if node.right:
            visited += self.traverse_preorder(node.right)
        return visited

    def traverse_inorder(self, node=None):
        if node is None:
            node = self.root
        visited = []
        if node.left:
            visited += self.traverse_inorder(node.left)
        visited += [node.key]
        if node.right:
            visited += self.traverse_inorder(node.right)
        return visited

    def traverse_postorder(self, node=None):
        if node is None:
            node = self.root
        visited = []
        if node.left:
            visited += self.traverse_postorder(node.left)
        if node.right:
            visited += self.traverse_postorder(node.right)
        visited += [node.key]
        return visited

    def traverse_preorder_stack(self):
        nodes = Stack()
        nodes.push(self.root)
        visited = []
        while not nodes.is_empty:
            node = nodes.pop()
            visited += [node.key]
            # Push the right node first, then the left node
            # to visit them in the correct order (left, right)
            # for a preorder traversal.
            if node.right:
                nodes.push(node.right)
            if node.left:
                nodes.push(node.left)
        return visited
