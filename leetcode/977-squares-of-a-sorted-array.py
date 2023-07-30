class Solution(object):

    def findSearchInsertPositionRecursive(self, nums, target, p1, p2):

        if p1 == p2:
            return p1

        mid = (p2 + p1)//2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            p1 = mid + 1

        if target < nums[mid]:
            p2 = mid

        return self.findSearchInsertPositionRecursive(nums, target, p1, p2)

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []

        for num in nums:
            square = num * num

            insert_idx = self.findSearchInsertPositionRecursive(result, square, 0, len(result))
            result.insert(insert_idx, square)

        return result


solution = Solution()
print("pass") if solution.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100] else print("false")
print("pass") if solution.sortedSquares([]) == [] else print("false")
print("pass") if solution.sortedSquares([5]) == [25] else print("false")
print("pass") if solution.sortedSquares([5, 5]) == [25, 25] else print("false")

# # print([1,2,3].insert(1, 100))
# n = [1, 2, 3]
# n.insert(1, 100)
# print(n)
