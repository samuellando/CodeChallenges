class Solution:
    def exist(self, board: List[List[str]], word: str, v = None, sr = None, sc = None) -> bool:
        if word == "":
            return True
        
        if v is None:
            v = [[False] * len(board[0]) for _ in range(len(board))] # visited.
        
        if sr is not None and sc is not None:  
            if not v[sr][sc] and board[sr][sc] == word[0]:
                if len(word) == 1:
                    return True
                v[sr][sc] = True
                # Down?
                if sr < len(board) - 1 and not v[sr+1][sc] and self.exist(board, word[1:], v, sr+1, sc):
                    return True
                # Up?
                if sr > 0 and not v[sr-1][sc] and self.exist(board, word[1:], v, sr-1, sc):
                    return True
                # Right?
                if sc < len(board[0]) - 1 and not v[sr][sc+1] and self.exist(board, word[1:], v, sr, sc+1):
                    return True
                # Left?
                if sc > 0 and not v[sr][sc-1] and self.exist(board, word[1:], v, sr, sc-1):
                    return True
                v[sr][sc] = False
        else:
            for i, row in enumerate(board):
                for j, l in enumerate(row):
                    if self.exist(board, word, v, i, j):
                        return True
        
        return False
