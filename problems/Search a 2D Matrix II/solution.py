class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int, sr = None, er = None, sc = None, ec = None) -> bool:
        sr = sr if sr is not None else 0
        er = er if er is not None else len(matrix) - 1
        sc = sc if sc is not None else 0
        ec = ec if ec is not None else len(matrix[0]) - 1
        
        while er >= sr and ec >= sc:
            midr = (sr + er) // 2
            midc = (sc + ec) // 2
            
            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] > target:
                return self.searchMatrix(matrix, target, sr, midr - 1, midc, ec) or self.searchMatrix(matrix, target, sr, er, sc, midc - 1)
            else:
                return self.searchMatrix(matrix, target, midr + 1, er, sc, midc) or self.searchMatrix(matrix, target, sr, er, midc + 1, ec)
        
        return False
