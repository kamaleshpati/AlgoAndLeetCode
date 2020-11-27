class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next


def printList(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def rotateList(head, k):
    if k == 0:
        return
    current = head
    count = 1
    while count < k and current is not None:
        current = current.next
        count += 1
    if current is None:
        return
    kthNode = current
    while (current.next is not None):
        current = current.next

    current.next = head
    head = kthNode.next
    kthNode.next = None
    print(head.data)


if __name__ == '__main__':
    llist = Linked_List()

    llist.insert([1, 2, 3, 4, 5, 6])

    printList(llist.head)
    rotateList(llist.head,4)
    printList(llist.head)
