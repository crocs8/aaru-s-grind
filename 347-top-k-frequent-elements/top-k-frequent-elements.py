class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans=[]
        for i in nums:
            freq[i] = freq.get(i, 0)+1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = [key for key, value in sorted_freq[:k]]
        return(ans)
