class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        return len(hash_map.values()) == len(set(hash_map.values()))
print(Solution().uniqueOccurrences([1, 2, 2]))  # True