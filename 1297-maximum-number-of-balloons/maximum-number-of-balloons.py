class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        #aryan
        b=a=l=o=n=0
        b=text.count('b')
        a=text.count('a')
        l=text.count('l')//2
        o=text.count('o')//2
        n=text.count('n')
        return min(b,a,l,o,n)