class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        if len(digits) == 0:
            return []
        
        res = [""]
        for d in digits:
            n = int(d)
            nres = []
            for c in letters[n]:
                for r in res:
                    nres.append(r+c)
            
            res = nres
        
        return res
