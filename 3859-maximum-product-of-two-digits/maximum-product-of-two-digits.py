class Solution:
    def maxProduct(self, n: int) -> int:
        m=str(n)
        ans=[]
        for i in m:
            ans.append(int(i))
        ans=sorted(ans)
        return ans[-1]*ans[-2]