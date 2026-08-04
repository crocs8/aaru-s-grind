class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in range(nums[0],nums[-1]):
            if i in nums:
                continue
            else: ans.append(i)
        return ans