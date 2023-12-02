# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        node = head

        numbers = []

        while node:
            numbers.append(node.val)
            node = node.next

        # print(numbers)

        p1 = 0
        p2 = len(numbers) - 1

        max_sum = 0

        while p1 < p2:
            a = numbers[p1]
            b = numbers[p2]

            c = a + b

            max_sum = max(max_sum, c)

            p1 += 1
            p2 -= 1

        return max_sum

solution = Solution()

head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print("Pass") if solution.pairSum(head) == 6 else print("Fail")

head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
print("Pass") if solution.pairSum(head) == 7 else print("Fail")

head = ListNode(1, ListNode(1000))
print("Pass") if solution.pairSum(head) == 1001 else print("Fail")

"""
Problem: maximum twin sum of a linked list
Type: stack

Thinking:
* traverse lined list and put values into array
* use two pointers and sum up the twins
* keep track of max_sum

Complexity:
* Time: O(N)
* Memory:O(N)
"""
