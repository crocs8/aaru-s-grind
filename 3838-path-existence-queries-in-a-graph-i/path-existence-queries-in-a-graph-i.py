class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        comp = [0] * n
        cid = 0
        prev = nums[0]

        for i in range(1, n):
            if nums[i] - prev > maxDiff:
                cid += 1
            comp[i] = cid
            prev = nums[i]

        return [comp[u] == comp[v] for u, v in queries]