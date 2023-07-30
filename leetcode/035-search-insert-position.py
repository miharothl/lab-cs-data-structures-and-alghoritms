class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        p1 = 0
        p2 = len(nums)

        return self.searchInsertRecursive(nums, target, p1, p2)

    def searchInsertRecursive(self, nums, target, p1, p2):

        mid = (p1 + p2) // 2

        if p1 == p2:
            return p1

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            p1 = mid + 1
        if target < nums[mid]:
            p2 = mid

        return self.searchInsertRecursive(nums, target, p1, p2)


nums = [1, 3, 5, 6]

solution = Solution()
print("pass") if solution.searchInsert(nums, 5) == 2 else print("fail")
print("pass") if solution.searchInsert(nums, 2) == 1 else print("fail")
print("pass") if solution.searchInsert(nums, 7) == 4 else print("fail")
