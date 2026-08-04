class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(min(nums),max(nums)):
            if i in nums:
                continue
            else: ans.append(i)
        return ans