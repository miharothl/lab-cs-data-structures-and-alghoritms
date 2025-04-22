# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # write index
        k = 0

        # read index
        i = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()

nums = [3, 2, 2, 3]
val = 3

nums = [3, 2, 2, 3]
k = solution.removeElement(nums, val = 2)
print("pass") if k == 2 else print("fail")
print(nums[:k])

nums = [0,1,2,2,3,0,4,2]
k = solution.removeElement(nums, val = 2)
print("pass") if k == 5 else print("fail")
print(nums[:k])
