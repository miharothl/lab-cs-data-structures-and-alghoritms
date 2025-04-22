# https://leetcode.com/problems/valid-palindrome/

# topics: two pointers, string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = [c.lower() for c in s if c.isalnum()]

        p1 = 0
        p2 = len(filtered) - 1

        while p1 < p2:
            if filtered[p1] != filtered[p2]:
                return False

            p1 += 1
            p2 -= 1

        return True



solution = Solution()

s = "A man, a plan, a canal: Panama"
print("pass") if solution.isPalindrome(s) == True else print("fail")

"""
Idea:
* filter out non alpha numeric chars
* iterate traversing the array using two pointers
** compare values at the both pointers 

Time Complexity
O(N) - one pass to clean one, one to compare

Space Complexity
O(1) - only variables for two pointers
"""