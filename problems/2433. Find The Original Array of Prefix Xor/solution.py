class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #perf[0] = arr[0]
        #perf[1] = arr[0] ^ arr[1]
        #perf[2] = arr[0] ^ arr[1] ^ arr[2]
        
        #so perf[i] = perf[i-1] ^ arr[i]
        #=> arr[i] = perf[i] ^ perf[i-1]
        
        arr = [pref[0]]
        
        i = 1
        while i < len(pref):
            arr.append(pref[i-1] ^ pref[i])
            i += 1
            
        return arr
