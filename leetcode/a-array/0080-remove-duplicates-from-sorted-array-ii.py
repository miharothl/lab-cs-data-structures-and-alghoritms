# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <=2:
            return len(nums)

        # write index
        k = 2

        for i in range(2, len(nums)):

            if nums[k-2] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k

solution = Solution()

nums = [1,1,1,2,2,3]
k = solution.removeDuplicates(nums)
print("pass") if k == 5 and nums[:k] == [1,1,2,2,3] else print("fail")

nums = [1,2]
k = solution.removeDuplicates(nums)
print("pass") if k == 2 and nums[:k] == [1,2] else print("fail")

nums = [1]
k = solution.removeDuplicates(nums)
print("pass") if k == 1 and nums[:k] == [1] else print("fail")


"""
Time: O(n)
Space: O(1)

Notes:
 * k is the write pointer.
 * nums[k - 2] is the second-most-recently-written value.
 * You compare nums[i] with nums[k - 2]:
 ** If they’re not equal, it's safe to keep nums[i] (it hasn’t appeared more than twice).
 ** If they’re equal, skip it.
"""