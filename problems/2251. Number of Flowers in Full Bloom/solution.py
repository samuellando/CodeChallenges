class Solution:
    def fullBloomFlowers(self, flowers, people):
        return self.updates(flowers, people)

    def updates(self, flowers, people):
        updates = {}
        # O(n)
        for f in flowers:
            updates[f[0]] = updates.get(f[0], 0) + 1
            updates[f[1]+1] = updates.get(f[1]+1, 0) - 1

        i = 0
        ans = [0] * len(people)
        # O(n log n)
        people = sorted(enumerate(people), key=lambda  x: x[1])
        count = 0
        t1 = 0
        # O(n)
        print(people)
        for t in sorted(updates.keys()):
            while i < len(people):
                if people[i][1] >= t1 and people[i][1] < t:
                    ans[people[i][0]] = count
                    i += 1
                else:
                    break

            count += updates[t]
            t1 = t
            print(t, count)

        return ans


        
    def naive(self, flowers, people):
        ans = [0] * len(people)
        for i, p in enumerate(people):
            for f in flowers:
                if p >= f[0] and p <= f[1]:
                    ans[i] += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    #print(s.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
    print(s.fullBloomFlowers([[1,10],[3,3]], [3,3,2]))
