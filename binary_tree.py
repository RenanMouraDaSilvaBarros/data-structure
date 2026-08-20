class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        # Se a árvore estiver vazia, o novo nó será a raiz.
        if self.root is None:
            self.root = new_node
            return

        parent = None
        current = self.root

        # Caminha até encontrar uma posição vazia.
        while current is not None:
            parent = current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Liga o novo nó ao último nó visitado.
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def show_pre_order(self, node):
        """Mostra: raiz, depois esquerda e, por fim, direita."""
        if node is not None:
            print(node.value)
            self.show_pre_order(node.left)
            self.show_pre_order(node.right)


tree = BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)

tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)

tree.show_pre_order(tree.root)
