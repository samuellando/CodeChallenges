class Solution:
    def isIsomorphic(self, s: str, t: str):
        ms = {}
        mt = {}
        for i in range(len(s)):
            if s[i] in ms:
                ms[s[i]].append(i)
            else:
                ms[s[i]] = [i]
                
            if t[i] in mt:
                mt[t[i]].append(i)
            else:
                mt[t[i]] = [i]
                
        for k in ms:
            i = ms[k][0]
            kt = t[i]
            if len(ms[k]) != len(mt[kt]):
                return False
            for i in range(len(ms[k])):
                if ms[k] != mt[kt]:
                    return False
            
        
        return True
