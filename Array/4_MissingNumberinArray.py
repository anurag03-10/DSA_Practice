#https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        lst = [x for x in range(len(nums) + 1)]
        for num in nums:
            if num in lst:
                lst.remove(num)
        return lst[0]