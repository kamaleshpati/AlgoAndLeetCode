class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def levelOrderTraversal(l1, l2):

    if len(l1) == 0:
        return

    for node in l1:
        print(node.data, end=" ")
        if node.left is not None:
            l2.append(node.left)
        if node.right is not None:
            l2.append(node.right)

    print()
    levelOrderTraversal(l2, [])


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    levelOrderTraversal([root], [])
