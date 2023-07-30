# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token == "+" or token == "-" or token == "*" or token == "/":
                n1 = stack.pop()
                n2 = stack.pop()

                if token == "+":
                    n = int(n1) + int(n2)
                    stack.append(n)
                if token == "*":
                    n = int(n1) * int(n2)
                    stack.append(n)
                if token == "/":
                    n = int(n2) / int(n1)
                    stack.append(int(n))
                if token == "-":
                    n = int(n2) - int(n1)
                    stack.append(int(n))
            else:
                stack.append(int(token))

        return stack.pop()


solution = Solution()

tokens = ["2", "1", "+"]
print("pass") if solution.evalRPN(tokens) == 3 else print("fail")

tokens = ["2", "1", "+", "3", "*"]
print("pass") if solution.evalRPN(tokens) == 9 else print("fail")

tokens = ["4", "13", "5", "/", "+"]
print("pass") if solution.evalRPN(tokens) == 6 else print("fail")

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print("pass") if solution.evalRPN(tokens) == 22 else print("fail")

tokens = ["18"]
print("pass") if solution.evalRPN(tokens) == 18 else print("fail")

tokens = ["0", "3", "/"]
print("pass") if solution.evalRPN(tokens) == 0 else print("fail")


"""
Problem: eval rpn
Type: stack

Thinking:
* use stack
* traverse array of tokens
* if not operator push to stack
* if operator pop from stack twice and use operator and push to stack

Complexity:
* Time: O(N)
* Memory:O(N)
"""
