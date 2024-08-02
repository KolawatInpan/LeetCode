class Solution:
    def maxOperations(self, nums: list, k: int) -> int:
        ans = 0
        hash_map = {}
        for num in nums:
            if k - num in hash_map and hash_map[k - num] > 0:
                ans += 1
                hash_map[k - num] -= 1
            else:
                if num not in hash_map:
                    hash_map[num] = 0
                hash_map[num] += 1
        return ans

print(Solution().maxOperations([3, 1,3,4,3], 6))  # 1