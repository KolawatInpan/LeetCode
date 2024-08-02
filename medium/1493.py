class Solution:
    def longestSubarray(self, nums: list) -> int:
        left = 0
        zero_available = 1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_available -= 1
            while zero_available < 0:
                if nums[left] == 0:
                    zero_available += 1
                left += 1
            res = max(res, i - left)
        return res
print(Solution().longestSubarray([0, 1,1,1,0,1,1,0,1]))  # 5
