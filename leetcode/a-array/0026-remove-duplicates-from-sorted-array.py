# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # write pointer
        k = 0

        val = nums[0]

        for i in range(0, len(nums)):

            if i == 0:
                val = nums[i]
                k += 1

            if nums[i] != val:
                val = nums[i]
                nums[k] = val
                k += 1

        return k


solution = Solution()

nums = [1,1,2]
k = solution.removeDuplicates(nums)
print("pass") if k == 2 else print("fail")
print(nums[:k])

nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)
print("pass") if k == 5 else print("fail")
print(nums[:k])
