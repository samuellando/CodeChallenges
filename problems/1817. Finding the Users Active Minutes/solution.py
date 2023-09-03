class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}

        for log in logs:
            if log[0] in users:
                users[log[0]][log[1]] = True
            else:
                users[log[0]] = {log[1]: True}
        
        a = [0] * k

        for user in users.values():
            a[len(user.keys()) - 1] += 1
        
        return a
