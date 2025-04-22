# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # work backwards from the end of nums1 and insert the largest elements from either nums1 or nums2,
        # avoiding overwriting data in nums1.

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1

        # Copy the remaining elements of nums2 into the front of nums1
        nums1[:p2 + 1]  = nums2[:p2 + 1]

        return nums1

solution = Solution()

print("pass") if solution.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6] else print("fail")
print("pass") if solution.merge([1], 1, [], 0) == [1] else print("fail")
print("pass") if solution.merge([1,2,3,0,0,0], 3, [0, 0, 0], 3) == [0, 0, 0, 1, 2, 3] else print("fail")
print("pass") if solution.merge([0], 0, [1], 1) == [1] else print("fail")