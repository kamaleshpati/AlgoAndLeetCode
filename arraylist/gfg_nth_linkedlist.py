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


def createList(arr, n):
    lis = Linked_List()
    for i in arr:
        lis.insert(i)
    return lis.head


def findNth(head, n):
    last = head
    start = head

    if head is not None:
        for i in range(n):
            if last is not None and last.next is not None:
                last = last.next
            else:
                return -1
        while last is not None and last.next is not None:
            last = last.next
            start = start.next

    else:
        return -1

    return start.data


if __name__ == '__main__':
    print(findNth(createList([2, 4, 6, 7, 5, 1], 6), 10))
