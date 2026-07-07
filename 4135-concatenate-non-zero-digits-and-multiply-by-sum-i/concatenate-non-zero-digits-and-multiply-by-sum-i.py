class Solution(object):
    def sumAndMultiply(self, n):
        c=0
        s=[]
        su=0
        res=0
        while n:
            if n%10>0:
                c=n%10
                s.append(c)
                n=n-c
            if n%10==0:
                n=n/10
        for i in range(len(s)):
            su=(s[i]*10**(i))
            res+=su
        return res*sum(s)