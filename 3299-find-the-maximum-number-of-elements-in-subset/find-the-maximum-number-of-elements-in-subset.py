class Solution(object):
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in cnt:
            if cnt[1] % 2:
                ans = max(ans, cnt[1])
            else:
                ans = max(ans, cnt[1] - 1)

        for x in cnt:
            if x == 1:
                continue

            length = 1
            cur = x

            while cnt[cur] >= 2:
                nxt = cur * cur
                if nxt not in cnt:
                    break
                length += 2
                cur = nxt

            ans = max(ans, length)

        return ans