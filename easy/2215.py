class Solution:
    def complement(self, nums1, nums2):
        return list(set(nums1) - set(nums2))
    def findDifference(self, nums1: list, nums2: list):
        return list([self.complement(nums1, nums2)] + [self.complement(nums2, nums1)])

print(Solution().findDifference([1, 2, 3], [2, 4, 6]))  # []