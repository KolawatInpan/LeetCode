class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1 = {}
        w2 = {}
        
        for i in word1:
            if i in w1:
                w1[i] += 1
            else:
                w1[i] = 1
        
        for i in word2:
            if i in w2:
                w2[i] += 1
            else:
                w2[i] = 1
                
        return sorted(w1.keys()) == sorted(w2.keys()) and sorted(w1.values()) == sorted(w2.values())

print(Solution().closeStrings("aa", "a"))  # True