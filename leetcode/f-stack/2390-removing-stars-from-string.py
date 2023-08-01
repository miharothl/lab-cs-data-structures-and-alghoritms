# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                stack.pop()

        # print(stack)

        return ''.join(ch for ch in stack)




solution = Solution()

s, res = "leet**cod*e", "lecoe"
print("Pass") if solution.removeStars(s) == res else print("Fail")

s, res = "erase*****", ""
print("Pass") if solution.removeStars(s) == res else print("Fail")

"""
Problem: remove stars from string
Type: stack

Thinking:
* for each element in string add to stack if not *, otherwise pop stack
* use string join() to join elements in stack back to result string

Complexity:
* Time: iterate through string, stack with N elements, in worst case scenario no * twice, O(N)
* Memory: create a stack for N, elements, O(N)
"""
