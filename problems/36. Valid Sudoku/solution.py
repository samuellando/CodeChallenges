def check(e, m):
    if e != ".":
        if not e in m:
            m[e] = True
        else:
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = board

        mb = [[{}, {}, {}] for i in range(3)]
        mr = [{} for i in range(9)]
        mc = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                if not (check(b[i][j], mr[i]) and check(b[i][j], mc[j]) and check(b[i][j], mb[i // 3][j // 3])):
                    return False
        return True

