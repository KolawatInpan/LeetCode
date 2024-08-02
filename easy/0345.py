class Solution:
    def reverseVowels(self, s: str) -> str:
        sl = list(s)
        vowel = "aeiouAEIOU"
        i, j = 0, len(sl) - 1
        while i < j:
            if sl[i] in vowel and sl[j] in vowel:
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
            else:
                if sl[i] not in vowel:
                    i += 1
                if sl[j] not in vowel:
                    j -= 1
        return "".join(sl)
