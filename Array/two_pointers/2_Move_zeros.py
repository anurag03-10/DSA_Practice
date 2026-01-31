#https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[x]=nums[i]
                x+=1
        nums[x:] = [0] * (len(nums) - (x))
        return nums