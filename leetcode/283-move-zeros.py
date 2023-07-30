class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # nums = self.reverse(nums)

        p_scan = 0
        p_replaced_zero = 0

        while p_scan < len(nums):
            if nums[p_scan] != 0:
                nums[p_scan], nums[p_replaced_zero] = nums[p_replaced_zero], nums[p_scan]
                p_replaced_zero += 1

            p_scan += 1

        # if len(nums) == 1:
        #     return nums

        # while True:
        #
        #     swap = False
        #
        #     while p0 < len(nums):
        #         if nums[p0] == 0:
        #             swap = True
        #             break
        #         p0 += 1
        #
        #     while p1 < len(nums):
        #         if nums[p1] != 0:
        #             break
        #         p1 += 1
        #
        #     if swap and p1 <= (len(nums) - 1):
        #         nums[p0] = nums[p1]
        #         nums[p1] = 0
        #
        #     if p0 == len(nums) or p1 == len(nums):
        #         break

        return nums


solution = Solution()

print("pass") if solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0] else print("fail")
print("pass") if solution.moveZeroes([0]) == [0] else print("fail")
print("pass") if solution.moveZeroes([0, 1]) == [1, 0] else print("fail")
print("pass") if solution.moveZeroes([1, 0]) == [1, 0] else print("fail")
print("pass") if solution.moveZeroes([1, 2]) == [1, 2] else print("fail")
