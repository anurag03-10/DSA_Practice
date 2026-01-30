#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        count = 0

        while current:
            count += 1
            current = current.next

        count -= n
        current = head
        prev = None

        for _ in range(count):
            prev = current
            current = current.next

        # if removing head
        if prev is None:
            return head.next

        prev.next = current.next
        return head


