class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiouAEIOU"
        max_vowels = sum([1 for i in s[:k] if i in vowel])
        curr_vowels = max_vowels
        for i in range(k, len(s)):
            curr_vowels += (1 if s[i] in vowel else 0) - (1 if s[i-k] in vowel else 0)
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
print(Solution().maxVowels("abciiidef", 3))  # 3