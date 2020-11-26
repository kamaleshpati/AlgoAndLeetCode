class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
    
class LinkedList:
    def __init__(self,head:Node): 
        self.head = head
        self.resultHead = None
        self.tail = None

    def reverse(self,k):
        temp = self.head
        # self.revNElements(temp,k)
        printList(self.revNElements(temp,k))
        
    
    def revNElements(self,head,k):
        curr = head
        prev = None
        count = 0
        tail = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count +=1
            if(count==1):
                tail = prev
            if(k==count):
                break
        if(k!=count):
            return self.revNElements(prev,count)

        if(curr is not None):
            tail.next = self.revNElements(curr,k)
            
        
        return prev

            




    

def printList(head): 
        temp = head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
    
llist = LinkedList(Node(1)) 
llist.head.next = Node(2) 
llist.head.next.next = Node(3)
llist.head.next.next.next = Node(4) 
llist.head.next.next.next.next = Node(5)
llist.head.next.next.next.next.next = Node(6) 
llist.head.next.next.next.next.next.next = Node(7)
llist.head.next.next.next.next.next.next.next = Node(8)


llist.reverse(3)




  