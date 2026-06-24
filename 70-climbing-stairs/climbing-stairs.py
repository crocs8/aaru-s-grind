class Solution(object):
    def climbStairs(self, n):
        fis=0
        nex=1
        for i in range(fis,n):
            res=fis+nex
            fis=nex
            nex=res
        return res

        