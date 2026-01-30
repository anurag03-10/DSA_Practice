#https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        
        if head is None or head.next is None:
            return 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected, now count the length
                count = 1
                temp = slow.next
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count
        return 0