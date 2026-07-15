class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd=-1
        even=0
        sumodd=0
        sumeven=0
        for i in range(n):
            odd+=2
            sumodd+=odd
            even+=2
            sumeven+=even
        return sumeven-sumodd