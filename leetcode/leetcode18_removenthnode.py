class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):

        tempHead = head
        tempHeadNext = head
        while n != 1:
            tempHeadNext = tempHeadNext.next
            n -= 1
        if tempHeadNext.next is None:
            head = tempHead.next
            return head
        temp = None
        while tempHeadNext.next is not None:
            tempHeadNext, temp, tempHead = tempHeadNext.next, tempHead, tempHead.next

        temp.next = tempHead.next
        tempHead.next = None
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    head = Solution().removeNthFromEnd(head, 2)
    while head is not None:
        print(head.val)
        head = head.next
