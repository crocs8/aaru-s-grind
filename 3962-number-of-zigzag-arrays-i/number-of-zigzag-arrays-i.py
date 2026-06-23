class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 1000000007
        m = r - l + 1

        up = [0] * (m + 1)
        down = [0] * (m + 1)

        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v

        for _ in range(3, n + 1):
            newUp = [0] * (m + 1)
            newDown = [0] * (m + 1)

            prefix = 0
            for v in range(1, m + 1):
                newUp[v] = prefix
                prefix = (prefix + down[v]) % MOD

            suffix = 0
            for v in range(m, 0, -1):
                newDown[v] = suffix
                suffix = (suffix + up[v]) % MOD

            up = newUp
            down = newDown

        ans = (sum(up) + sum(down)) % MOD
        return ans