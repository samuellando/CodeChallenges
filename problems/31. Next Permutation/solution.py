class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find the first element with a higher element to the right
        flip = len(nums) - 1
        maximum = nums[flip]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < maximum:
                flip = i
                break
            elif nums[i] > maximum:
                maximum = nums[i]
        else:
            nums.reverse()
            return

        # Now find the next min, and swap it
        m = -1
        for i in range(flip + 1, len(nums)):
            if (m == -1 or nums[i] < nums[m]) and nums[i] > nums[flip]:
                m = i

        t = nums[flip]
        nums[flip] = nums[m]
        nums[m] = t

        # Heapsort the reamining elements
        heap = []
        for n in nums[flip+1:]:
            heapq.heappush(heap, n)
        for i in range(flip+1, len(nums)):
            nums[i] = heapq.heappop(heap)
