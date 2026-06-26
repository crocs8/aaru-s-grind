from collections import defaultdict

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        counts = defaultdict(int)
        counts[0] = 1
        current_sum = 0
        smaller_counts = 0
        ans = 0
        for num in nums:
            if num == target:
                smaller_counts += counts[current_sum]
                current_sum += 1
            else:
                current_sum -= 1
                smaller_counts -= counts[current_sum]
            ans += smaller_counts
            counts[current_sum] += 1
        return ans