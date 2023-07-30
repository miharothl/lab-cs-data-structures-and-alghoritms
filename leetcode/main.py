class Solution(object):
    def search(self, nums, target):
        """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

        p1 = 0
        p2 = len(nums) - 1

        if p2 < p1:
            return -1

        return self.search_recursive(nums, target, p1, p2, 0)

    def search_recursive(self, nums, target, p1, p2, level):
        s = p1 + int((p2 - p1) / 2)

        if level > 3:
            return -100

        current = nums[s]

        if current == target:
            return s

        if p1 == p2:
            return -1

        if target > current:
            p1 = s + 1

        if target < current:
            p2 = s

        level = level + 1

        return self.search_recursive(nums, target, p1, p2, level)

nums = [-1, 0, 3, 5, 9, 12]

solution = Solution()
print("pass") if solution.search(nums, 9) == 4 else print("fail")
print("pass") if solution.search(nums, 2) == -1 else print("fail")
print("pass") if solution.search([1], 2) == -1 else print("fail")
print("pass") if solution.search([], 2) == -1 else print("fail")
