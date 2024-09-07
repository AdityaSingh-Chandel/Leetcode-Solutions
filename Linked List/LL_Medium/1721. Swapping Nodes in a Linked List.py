                   # 18-08-24

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n=0
        curr=head
        while curr:
            curr=curr.next
            n+=1
        le=head
        ri=head
        for i in range(1,k):
            le=le.next
        for _ in range(1,n-k+1):
            ri=ri.next
        # swap
        le.val,ri.val=ri.val,le.val
        return head