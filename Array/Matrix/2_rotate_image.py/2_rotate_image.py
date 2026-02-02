#https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, nums):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(nums)
        column = len(nums[0])

        for i in range(row):
            for j in range(i+1,column):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        
        for k in range(row):
            nums[k].reverse()