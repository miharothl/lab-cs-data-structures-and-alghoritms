# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        start = 0
        result = []

        for i in range(len(nums)-1):

            # detect if not range
            if nums[i] + 1 != nums[i+1]:
                end = i

                if start == end:
                    result.append(f"{nums[start]}")
                else:
                    result.append(f"{nums[start]}->{nums[end]}")

                start = i+1 ## if so reset start pointer

        if start == len(nums) - 1:
            result.append(f"{nums[start]}")
        else:
            result.append(f"{nums[start]}->{nums[len(nums)-1]}")

        return result

solution = Solution()

nums = []
print("pass") if solution.summaryRanges(nums) == [] else print("fail")

nums = [0,1,2,4,5,7]
print("pass") if solution.summaryRanges(nums) == ["0->2","4->5","7"] else print("fail")

nums = [0,2,3,4,6,8,9]
print("pass") if solution.summaryRanges(nums) == ["0","2->4","6","8->9"] else print("fail")



"""
Idea:
two pointers

Time:
O(n) - one pass

Space:
O(1) best case
O(n) worst case, if no ranges are found

"""