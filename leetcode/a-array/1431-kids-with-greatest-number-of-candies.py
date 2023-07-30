# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_current = max(candies)

        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_current:
                result.append(True)
            else:
                result.append(False)

        return result


solution = Solution()

print('Pass') if solution.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True] else print('Fail')
print('Pass') if solution.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False] else print('Fail')
print('Pass') if solution.kidsWithCandies([12, 1, 12], 10) == [True, False, True] else print('Fail')
