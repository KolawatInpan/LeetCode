class Solution:
    def isValid(self, s: str) -> bool:
        paren_mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in range(len(s)):
            if s[i] in paren_mapping:
                stack.append(s[i])
            else:
                if not stack or paren_mapping[stack.pop()] != s[i]:
                    return False
        return not stack
