#https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head
        count=0
        while current:
            current=current.next
            count+=1
        count= count//2
        current=head
        for _ in range(count):
            current=current.next
        
        return current