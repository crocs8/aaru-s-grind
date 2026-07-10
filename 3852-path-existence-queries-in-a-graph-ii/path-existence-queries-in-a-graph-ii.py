class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        values = []

        for i, (v, idx) in enumerate(arr):
            values.append(v)
            pos[idx] = i

        reach = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            reach[l] = r

        LOG = n.bit_length()
        jump = [reach]

        for _ in range(1, LOG):
            prev = jump[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            jump.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < b:
                    cur = jump[k][cur]
                    steps += 1 << k

            if reach[cur] < b:
                ans.append(-1)
            else:
                ans.append(steps + 1)

        return ans