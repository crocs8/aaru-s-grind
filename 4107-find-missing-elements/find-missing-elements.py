class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        j=0
        for i in range(nums[0],nums[-1]):
            if nums[j]!=i:
                ans.append(i)
            else: j+=1
        return ans