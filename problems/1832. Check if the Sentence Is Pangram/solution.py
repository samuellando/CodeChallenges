class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence
        s = s.lower()
        
        d = {}
        for c in s:
            d[c] = True
        
        for i in range(97, 123):
            if d.get(chr(i)) is None:
                return False
        
        return True
            
        
