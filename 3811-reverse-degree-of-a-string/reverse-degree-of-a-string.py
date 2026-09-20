class Solution:
    def reverseDegree(self, s: str) -> int:
        #97 to 122
        c=0
        for i in range(len(s)):
            a=122-ord(s[i])+1
            c+=a*(i+1)
        return c
    