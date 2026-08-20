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

    def show_tree(self):
        """Desenha a árvore no terminal, com a raiz no topo."""
        if self.root is None:
            print("Árvore vazia")
            return

        height = self._height(self.root)
        # Uma largura menor deixa o desenho compacto no terminal.
        width = 2 ** height
        nodes = [self.root]

        for level in range(height):
            positions = [
                (2 * index + 1) * width // (2 ** (level + 1))
                for index in range(2 ** level)
            ]
            self._print_values(nodes, positions, width)

            if level < height - 1:
                self._print_branches(nodes, positions, width)

            nodes = [
                child
                for node in nodes
                for child in (
                    (node.left if node is not None else None),
                    (node.right if node is not None else None),
                )
            ]

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def _print_values(self, nodes, positions, width):
        line = [" "] * width
        for node, position in zip(nodes, positions):
            if node is not None:
                value = str(node.value)
                start = position - len(value) // 2
                line[start:start + len(value)] = value
        print("".join(line).rstrip())

    def _print_branches(self, nodes, positions, width):
        line = [" "] * width
        for node, position in zip(nodes, positions):
            distance = width // (2 * len(positions))
            if node is not None and node.left is not None:
                line[position - distance // 2] = "/"
            if node is not None and node.right is not None:
                line[position + distance // 2] = "\\"
        print("".join(line).rstrip())


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

print("Pré-ordem:")
tree.show_pre_order(tree.root)

print("\nÁrvore:")
tree.show_tree()
