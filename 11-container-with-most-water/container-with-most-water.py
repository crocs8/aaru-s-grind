class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maxarea=0
        area=0
        while left<right:
            width=right-left
            area=min(height[left],height[right])*width
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea