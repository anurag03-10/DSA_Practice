#https://leetcode.com/problems/container-with-most-water/submissions/1903461206/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        mArea=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            mArea=max(mArea,h*w)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mArea