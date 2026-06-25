class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        offset = n + 1
        size = 2 * n + 3

        bit = Fenwick(size)

        prefix = 0
        ans = 0

        bit.update(offset + 1, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset + 1

            ans += bit.query(idx - 1)

            bit.update(idx, 1)

        return ans