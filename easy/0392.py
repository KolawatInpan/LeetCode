class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        if not s:
            return not s
        for i in list(t):
            if not s:
                return not s
            if i == s[0]:
                s.pop(0)
        return not s
