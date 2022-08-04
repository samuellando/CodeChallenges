class Solution:
        def numberOfBeams(self, bank):

            beams = 0
            s = 0
            for r in bank:
                d = 0
                for c in r:
                    if c == "1":
                        d = d + 1
                beams = beams + s * d
                if d != 0:
                    s = d
            return beams








if __name__ == "__main__":
    s = Solution()

    i = ["011001","000000","010100","001000"] 
    i2 = ["000","111","000"] 

    print(s.numberOfBeams(i2))
