class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # So two strings are similar if:
        # They have the same count set, and character set.
        
        if len(word1) != len(word2):
            return False
        
        d1 = {}
        for c in word1:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        
        d2 = {}
        for c in word2:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        
        c1 = list(d1.values())
        c2 = list(d2.values())
        
        k1 = list(d1.keys())
        k2 = list(d2.keys())
        
        c1.sort()
        c2.sort()
        k1.sort()
        k2.sort()

        return c1 == c2 and k1 == k2
