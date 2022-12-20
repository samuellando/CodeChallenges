class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = [False] * len(rooms)

        s = [0]


        while len(s) > 0:
            p = s.pop(0)
            v[p] = True

            for key in rooms[p]:
                if not v[key]:
                    s.insert(0, key)

        for room in v:
            if not room:
                return False

        return True
