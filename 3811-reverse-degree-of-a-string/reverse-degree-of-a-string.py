class Solution:
    def reverseDegree(self, s: str) -> int:
        #97 to 122
        b=[]
        for i in range(len(s)):
            a=122-ord(s[i])+1
            c=a*(i+1)
            b.append(c)
        print(b)
        return sum(b)
    