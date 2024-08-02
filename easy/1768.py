class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_l = list(word1)
        w2_l = list(word2)
        ans = ""
        n_iters = max(len(word1), len(word2))
        for i in range(n_iters):
            if w1_l:
                ans += w1_l.pop(0)
            if w2_l:
                ans += w2_l.pop(0)
        return ans
