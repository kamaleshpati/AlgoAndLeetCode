class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode((l1.val + l2.val) % 10)
        self.addIterative(l1.next, l2.next, l3, (l1.val + l2.val) // 10)
        return l3

    def addIterative(self, l1: ListNode, l2: ListNode, l3: ListNode, extra=0):
        if l1 is not None and l2 is not None:
            l3.next = ListNode((l1.val + l2.val + extra) % 10)
            return self.addIterative(l1.next, l2.next, l3.next, (l1.val + l2.val + extra) // 10)
        elif l1 is not None and l2 is None:
            l3.next = ListNode((l1.val + extra) % 10)
            return self.addIterative(l1.next, l2, l3.next, (l1.val + extra) // 10)

        elif l1 is None and l2 is not None:
            l3.next = ListNode((l2.val + extra) % 10)
            return self.addIterative(l1, l2.next, l3.next, (l2.val + extra) // 10)
        else:
            if extra is not 0:
                l3.next = ListNode(extra)
            return


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    sol = Solution().addTwoNumbers(l1, l2)
    print(sol.val)
    print(sol.next.val)
    print(sol.next.next.val)
    print(sol.next.next.next.val)
