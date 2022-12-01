class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiou"
        
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        
        ac = 0
        bc = 0
        
        for c in a:
            if c.lower() in vowels:
                ac += 1
  
        for c in b:
            if c.lower() in vowels:
                bc += 1
            
        return ac == bc
