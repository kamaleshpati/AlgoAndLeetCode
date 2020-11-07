class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)




