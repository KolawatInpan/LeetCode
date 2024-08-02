class Solution:
    def productExceptSelf(self, nums) -> list:
        n = len(nums)
        ans = [1] * n
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            ans[i] *= left

        right = 1
        for i in range(n - 2, -1, -1):
            right *= nums[i + 1]
            ans[i] *= right
        return ans
