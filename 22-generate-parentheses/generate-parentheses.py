class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(s, open_count, close_count):
            # Complete valid combination
            if len(s) == 2 * n:
                ans.append(s)
                return

            # Add opening bracket
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add closing bracket
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return ans