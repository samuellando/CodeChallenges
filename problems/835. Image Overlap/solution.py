class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        a_1 = []
        b_1 = []
        
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    a_1.append((i,j))
                if img2[i][j] == 1:
                    b_1.append((i,j))
        
        d = {}
        
        ans = 0
        
        for x_1, y_1 in a_1:
            for x_2, y_2 in b_1:
                t = (x_1-x_2, y_1-y_2)
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1
                
                if d[t] > ans:
                    ans = d[t]
        
        return ans
                    
