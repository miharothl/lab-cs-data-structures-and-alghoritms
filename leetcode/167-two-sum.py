class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        pl = 0
        ph = len(numbers) - 1

        while pl < ph:
            if numbers[pl] + numbers[ph] == target:
                break

            if numbers[pl] + numbers[ph] > target:
                ph -= 1

            if numbers[pl] + numbers[ph] < target:
                pl += 1

        return [pl + 1, ph + 1]

solution = Solution()
print("pass") if solution.twoSum([5, 25, 75], 100) == [2, 3] else print("fail")
print("pass") if solution.twoSum([2, 7, 11, 15], 9) == [1, 2] else print("fail")
print("pass") if solution.twoSum([1, 2, 3, 4, 6], 6) == [2, 4] else print("fail")
print("pass") if solution.twoSum([2, 3, 4], 6) == [1, 3] else print("fail")
print("pass") if solution.twoSum([-1, 0], -1) == [1, 2] else print("fail")
