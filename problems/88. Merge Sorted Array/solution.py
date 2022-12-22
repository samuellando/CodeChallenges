class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        p1 = 0
        p2 = 0
        po = 0

        while p1 < m:
            nums1[len(nums1) - m + p1] = nums1[p1]
            p1 += 1
        
        p1 = m if m == 0 else 1

        while po < len(nums1):
            print(p1, p2, po)
            if p2 == len(nums2) or (p1 < len(nums1) and nums1[p1] <= nums2[p2]):
                nums1[po] = nums1[p1]
                p1 += 1
                po += 1
            else:
                nums1[po] = nums2[p2]
                p2 += 1
                po += 1
