#https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, x):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low + (high - low)//2
            if nums[mid]==x:
                return mid
            elif nums[mid]<=x:
                low = mid + 1
            else:
                high = mid -1
        return -1