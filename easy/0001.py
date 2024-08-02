class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in hashTable:
                return [hashTable[target - nums[i]], i]
            hashTable[nums[i]] = i
        return []
