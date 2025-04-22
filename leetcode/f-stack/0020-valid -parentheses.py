# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = { '}': '{', ')': '(', ']': '['}

        for char in s:

            if char in mapping:
                # close bracket
                top = stack.pop() if stack else ''

                if top != mapping[char]:
                    return False

                # if len(stack) > 0:
                #     top = stack.pop()
                #     if top != mapping[char]:
                #         return False
                # else:
                #     return False

            else:
                # open bracket
                stack.append(char)

        # return True
        return not stack


solution = Solution()

s = "()"
print("pass") if solution.isValid(s) == True else print("fail")

s = "([]){}"
print("pass") if solution.isValid(s) == True else print("fail")

s = "([){}]"
print("pass") if solution.isValid(s) == False else print("fail")

s = "("
print("pass") if solution.isValid(s) == False else print("fail")

s = ")"
print("pass") if solution.isValid(s) == False else print("fail")

"""
Idea:
* use stack to track opening brackets
* use hash to map opening and closing brackets 
* if closing bracket, check if matches top of the stack
** if it doesn't return False
* at the end if the stack is empty return True

Time Complexity
O{n} - one pass through array

Space Complexity
O{n} - stack - worst case all opening brackets go into the stack
"""
