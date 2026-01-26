#'https://www.geeksforgeeks.org/problems/second-largest3735/1'

class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        secLargest = float('-inf')
        
        for x in arr:
            if x > largest:
                largest = x
        
        for x in arr:
            if x > secLargest and x != largest:
                secLargest = x
        return secLargest if secLargest != float('-inf') else -1