#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        x=1
        for i in range(1,n):
            if nums[i-1]==nums[i]:
                pass
            else:
                nums[x]=nums[i]
                x+=1
        return x
