# https://leetcode.com/problems/majority-element


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)

        return candidate

    def majorityElement_usingHashTable(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1

        return max(counter, key=counter.get)



solution = Solution()

nums = [3,2,3]
print("pass") if solution.majorityElement(nums) == 3 else print("fail")

"""
# How it works
  * https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
 
  * You keep a count and a current candidate.
  * If the count drops to 0, you change the candidate.
  * The count increases if the current element matches the candidate and decreases otherwise.
  * Since the majority element appears more than n/2 times, it will be the last candidate left. 
  
# Time Complexity
  * O(n)

# Space Complexity
  * O(1)
"""

nums = [3,2,3]
print("pass") if solution.majorityElement_usingHashTable(nums) == 3 else print("fail")

"""
# How it works

# Time Complexity
  * O(n)

# Space Complexity
  * O(n)
"""

