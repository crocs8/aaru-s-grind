class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res=[nums[0]]
        j=1
        for i in range(len(nums)-1):
            if nums[j]!=nums[i]+1:
                break
            if nums[j]==nums[i]+1 and nums[i] not in res:
                res.append(nums[i])
                res.append(nums[j])
            elif nums[j]==nums[i]+1 and nums[i]  in res:
                res.append(nums[j])
            j+=1
        print(res)
        ans=sum(res)
        while ans in nums:
           ans += 1
        return ans