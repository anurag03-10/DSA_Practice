#https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0

class Solution:
    def largest(self, arr):
        # code here
        l=float('-inf')
        for x in arr:
            if x>l:
                l=x
        return l