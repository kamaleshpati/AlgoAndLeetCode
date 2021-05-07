class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        prev = None
        count = 0
        tail = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
            if (count == 1):
                tail = prev
            if (k == count):
                break
        if (k != count):
            return self.reverseKGroup(prev, count)

        if (curr is not None):
            tail.next = self.reverseKGroup(curr, k)

        return prev