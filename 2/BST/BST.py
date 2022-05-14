class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key

class BST:
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, node = None):
        if node:
            self.inorder_tree_walk(node.left)
            print(node.key, end=' ')
            self.inorder_tree_walk(node.right)

    def preorder_tree_walk(self, node = None):
        if node:
            print(node.key, end=' ')
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)

    def postorder_tree_walk(self, node = None):
        if node:
            self.postorder_tree_walk(node.left)
            self.postorder_tree_walk(node.right)
            print(node.key, end=' ')

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            current_parent = None
            current = self.root
            while current:
                current_parent = current
                if node.key < current.key:
                    current = current.left
                else:
                    current = current.right
            node.parent = current_parent
            if not current_parent:
                self.root = node
            elif node.key < current_parent.key:
                current_parent.left = node
            else:
                current_parent.right = node

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, node):
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            if y.parent is not node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def search(self, key):

        def search_(node, key):
            if not node or node.key is key:
                return node
            
            if key < node.key:
                return search_(node.left, key)
            else:
                return search_(node.right, key)
            
        return search_(self.root, key)

    def minimum(self, node = None):
        if not node:
            node = self.root
        while node.left:
            node = node.left
        return node

    def maximum(self, node = None):
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        current = node.parent
        while current and node is current.right:
            node = current
            current = current.parent
        return current

    def predeccessor(self, node):
        if node.left:
            return self.maximum(node.left)
        current = node.parent
        while current and node is current.left:
            node = current
            current = current.parent
        return current

def run():
    tree = BST()

    array = [1, 4, 2, 3]
    for number in array:
        node = Node(number)
        tree.insert(node)

    tree.inorder_tree_walk(tree.root)

    print()

    node = tree.search(2)
    print(tree.successor(node).key)

    print()

    delete = [2, 3]
    for number in delete:
        node = tree.search(number)
        tree.delete(node)

    tree.inorder_tree_walk(tree.root)

if __name__ == '__main__':
    run()