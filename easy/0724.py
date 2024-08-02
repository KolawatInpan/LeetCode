class Solution:
    def pivotIndex(self, nums: list) -> int:
        left_sum = 0
        total = sum(nums)
        right_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # 3