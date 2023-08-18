class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # turn the array into a hashmap, so we can quickly check if a vlaue is there.
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        
        # for each number, and search for 2 numbers that add up 0 - number.
        for num in m.keys():
            if m[num] != 0:
                m[num] -= 1
                m2 = m.copy()
                for num2 in m2.keys():
                    if m2[num2] != 0:
                        m2[num2] -= 1
                        need = 0 - (num + num2)
                        if m2.get(need, 0) != 0:
                            result.append([num, num2, need])
                        m2[num2] = 0
            
            m[num] = 0
        
        return result
                        
