# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#
#         result = list(nums)
#
#         for i in range(len(nums)):
#             val = nums[i]
#             j = (i+k) % len(nums)
#             result[j] = val
#
#         return result
# import math


def math_gcd(a, b):
    if b == 0:
        return a
    else:
        return math_gcd(b, a % b)


class Solution(object):


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        gcd = math_gcd(len(nums), k)

        for i in range(gcd):

            tmp = nums[i]

            j = i
            while True:
                d = (j + k) % len(nums)
                if d == i:
                    break
                nums[j] = nums[d]
                j = d

            nums[j] = tmp

        return nums


solution = Solution()
print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))

# print("pass") if solution.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4] else print("fail")
# print("pass") if solution.rotate([1, 2, 3, 4, 5, 6, 7], 0) == [1, 2, 3, 4, 5, 6, 7] else print("fail")
# print("pass") if solution.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100] else print("fail")
# print("pass") if solution.rotate([], 0) == [] else print("fail")


# def leftRotate(arr, d, n):
#     d = d % n
#     g_c_d = gcd(d, n)
#     for i in range(g_c_d):
#
#         # move i-th values of blocks
#         temp = arr[i]
#         j = i
#         while 1:
#             k = j + d
#             if k >= n:
#                 k = k - n
#             if k == i:
#                 break
#             arr[j] = arr[k]
#             j = k
#         arr[j] = temp
#
#
# # UTILITY FUNCTIONS
# # function to print an array
#
#
# def printArray(arr, size):
#     for i in range(size):
#         print("% d" % arr[i], end=" ")
#
#
# # Function to get gcd of a and b
#
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# # Driver program to test above functions
# arr = [1, 2, 3, 4, 5, 6, 7]
# n = len(arr)
# d = 2
# leftRotate(arr, d, n)
# printArray(arr, n)