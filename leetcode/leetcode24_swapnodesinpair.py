class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = head
        if temp is None:
            return head
        while temp is not None and temp.next is not None:
            temp.val, temp.next.val = temp.next.val, temp.val
            if temp.next.next is not None:
                temp = temp.next.next
            else:
                break
        return head

    def printList(self, head):
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    p = Solution()
    print(p.printList(p.swapPairs(l)))
