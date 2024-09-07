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
        dummy=ListNode()
        curr=dummy

        curr1=l1
        curr2=l2
        car=0

        while curr1 or curr2 or car:
            if curr1:
                val1=curr1.val
                curr1=curr1.next
            else:
                val1=0
            if curr2:
                val2=curr2.val
                curr2=curr2.next
            else:
                val2=0
            
            dig=val1+val2+car
            car=dig // 10
            d=dig % 10

            curr.next=ListNode(d)
            curr=curr.next
        return dummy.next
    
            
'''
# Driver Code

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)


obj=Solution()

print(obj.addTwoNumbers(l1, l2))
'''
