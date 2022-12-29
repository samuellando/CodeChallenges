import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        a = []

        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort()

        t = 1

        pq = []
        while len(tasks) > 0 or len(pq) > 0:
            if len(tasks) > 0 and len(pq) == 0 and t < tasks[0][0]:
                t = tasks[0][0]
                
            while len(tasks) > 0 and tasks[0][0] <= t:
                del tasks[0][0]
                heapq.heappush(pq, tasks[0])
                tasks.pop(0)
            
            task = heapq.heappop(pq)
            a.append(task[1])
            t += task[0]
        
        return a

