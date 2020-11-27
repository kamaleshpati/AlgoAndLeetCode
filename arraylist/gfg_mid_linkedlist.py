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


def findMid(head):
    last = head
    mid = head
    if head is not None:
        while last is not None and last.next is not None:
            last = last.next.next
            mid = mid.next

    return mid.data


if __name__ == '__main__':
    print(findMid(createList([2,4,6,7,5,1], 6)))
