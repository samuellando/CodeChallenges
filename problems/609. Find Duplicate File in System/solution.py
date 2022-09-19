class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = {} # Hashmap by contents
        
        for p in paths:
            l = p.split(" ")
            path = l[0]
            for f in l[1:]:
                content = f.split("(")[1].split(")")[0]
                if content in m:
                    m[content].append(path+"/"+f.split("(")[0])
                else:
                    m[content] = [path+"/"+f.split("(")[0]]
        
        out = []
        for l in m.values():
            if len(l) > 1:
                out.append(l)
        
        return out          
