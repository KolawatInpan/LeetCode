class Solution:
    def longestOnes(self, nums: list, k: int) -> int:
        ans = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6