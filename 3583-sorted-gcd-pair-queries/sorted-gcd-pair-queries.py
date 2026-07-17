from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        maxV = max(nums)
        freq = [0] * (maxV + 1)
        for v in nums:
            freq[v] += 1

        # cntMultiple[g] = number of elements divisible by g
        cntMultiple = [0] * (maxV + 1)
        for g in range(1, maxV + 1):
            s = 0
            for m in range(g, maxV + 1, g):
                s += freq[m]
            cntMultiple[g] = s

        # exact[g] = number of pairs whose gcd is exactly g
        exact = [0] * (maxV + 1)
        for g in range(maxV, 0, -1):
            c = cntMultiple[g]
            total = c * (c - 1) // 2
            for m in range(2 * g, maxV + 1, g):
                total -= exact[m]
            exact[g] = total

        # prefix[g] = number of pairs with gcd <= g
        prefix = [0] * (maxV + 1)
        for g in range(1, maxV + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []
        for q in queries:
            # find smallest g such that prefix[g] > q
            lo, hi = 1, maxV
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)
        return ans
        