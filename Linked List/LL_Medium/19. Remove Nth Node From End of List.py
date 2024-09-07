                  # 18-08-24
                  
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None
        first=head
        for i in range(n+1):
            # Important-----
            if first is None:
                head=head.next
                return head
            # ------------------
            first=first.next
        
        sec=head
        while first: # and first.next:
            first=first.next
            sec=sec.next
        sec.next=sec.next.next

        return head



        