class Solution(object):
    def merge(self, nums1, m, nums2, n):
        r = m + n - 1

        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[r] = nums1[m-1]
                m -= 1
            else:
                nums1[r] = nums2[n-1]
                n -= 1
            r -= 1
        