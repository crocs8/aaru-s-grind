class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            # pop larger chars that appear later again
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)