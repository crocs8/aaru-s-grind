class Solution(object):
    def arrayRankTransform(self, arr):
        ca=sorted(arr)
        rank={}
        j=1
        for i in ca:
            if i not in rank:
                rank[i]=j
                j+=1
            else:
                continue
        for i in range(len(arr)):
                arr[i]=rank[arr[i]]
        return arr        