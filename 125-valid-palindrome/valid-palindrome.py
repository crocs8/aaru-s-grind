class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        a=[]
        for i in range(len(s)):
            ans=s[i].isalnum()
            if ans ==True:
                a.append(s[i])
        r_a=a[::-1]
        if(a==r_a):
            return True
        return False