# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


solution = Solution()

# Input: head = [3,2,0,-4], pos = 1
# Output: true

nodes = [ListNode(i) for i in [3, 2, 0, -4]]

nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
nodes[3].next = nodes[1]

head = nodes[0]

print("pass") if solution.hasCycle(head) == True else print("fail")

# Input: head = [3,2], pos =-1
# Output: false

nodes = [ListNode(i) for i in [3, 2]]

nodes[0].next = nodes[1]
head = nodes[0]
print("pass") if solution.hasCycle(head) == False else print("fail")
