class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        right=0
        currentSum=0
        length=0
        minLen=float('inf')
        for i in range(len(nums)):
            currentSum+=nums[right]
            right+=1
            while currentSum>=target:
                length=(right-left)
                currentSum-=nums[left]
                left+=1
                minLen = min(minLen, length)
        if minLen==float('inf'):
            return 0
        else: return minLen