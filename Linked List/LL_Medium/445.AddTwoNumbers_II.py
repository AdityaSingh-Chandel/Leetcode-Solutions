                # 17-08-24
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1=self.rever(l1)
        l2=self.rever(l2)

        head=ListNode()
        curr=head
        car=0

        while l1 or l2 or car:
            if l1:
                val1=l1.val
                l1=l1.next
            else:
                val1=0
            if l2:
                val2=l2.val
                l2=l2.next
            else:
                val2=0
            
            dig= val1 + val2  + car
            car=dig//10
            d=dig%10

            curr.next=ListNode(d)
            curr=curr.next
        head=head.next

        return self.rever(head)
        
    def rever(self,head):
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        head=prev
        return head

