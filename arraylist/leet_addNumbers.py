class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # return self.findNumber(l1)+self.findNumber(l2)
        extra = (l1.val + l2.val)//10
        ans = ListNode((l1.val + l2.val)%10)
        res = ans
        l1 = l1.next
        l2 = l2.next
        while l1 != None and l2!=None:
            ans.next = ListNode((l1.val + l2.val+extra)%10)
            extra = (l1.val + l2.val+extra)//10
            l1 = l1.next
            l2 = l2.next
            ans = ans.next
        
        
        if l1!= None:
            while l1 != None:
                ans.next = ListNode((l1.val+extra)%10)
                extra = (l1.val +extra)//10
                l1 = l1.next
                ans = ans.next

        elif l2!= None:
            while l2 != None:
                ans.next = ListNode((l2.val+extra)%10)
                extra = (l2.val+extra)//10
                l2 = l2.next
                ans = ans.next
        
        if extra > 0:
            ans.next = ListNode(extra)

       
        return res


l1 = ListNode(9)
l1.next = ListNode(9)
# l1.next.next = ListNode(3)

l2 = ListNode(1)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

res = Solution().addTwoNumbers(l1,l2)

while res !=None:
    print(res.val)
    res = res.next