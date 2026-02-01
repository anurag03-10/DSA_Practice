#https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right =0, len(height)-1
        leftM, rightM = 0,0
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>leftM:
                    leftM=height[left]
                else:
                    water += leftM - height[left]
                left +=1
            else:
                if height[right]>rightM:
                    rightM = height[right]
                else:
                    water += rightM - height[right]
                right -= 1
        return water