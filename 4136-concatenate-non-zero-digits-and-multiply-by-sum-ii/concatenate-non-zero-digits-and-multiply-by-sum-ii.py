class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        # pow10[i] = 10^i % MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix arrays
        prefix_num = [0] * (n + 1)      # concatenated non-zero digits
        prefix_sum = [0] * (n + 1)      # sum of digits
        prefix_count = [0] * (n + 1)    # count of non-zero digits

        for i in range(1, n + 1):
            d = ord(s[i - 1]) - ord('0')

            prefix_sum[i] = prefix_sum[i - 1] + d
            prefix_count[i] = prefix_count[i - 1]

            if d != 0:
                prefix_count[i] += 1
                prefix_num[i] = (prefix_num[i - 1] * 10 + d) % MOD
            else:
                prefix_num[i] = prefix_num[i - 1]

        ans = []

        for l, r in queries:
            # Sum of digits in substring
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            # Number of non-zero digits
            cnt = prefix_count[r + 1] - prefix_count[l]

            # Concatenated number of non-zero digits
            x = (
                prefix_num[r + 1]
                - (prefix_num[l] * pow10[cnt]) % MOD
            ) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans