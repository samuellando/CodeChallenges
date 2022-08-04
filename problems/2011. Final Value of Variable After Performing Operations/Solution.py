class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        x = 0
        for o in operations:
            if "++" in o:
                x = x + 1
            else:
                x = x - 1
        return x
