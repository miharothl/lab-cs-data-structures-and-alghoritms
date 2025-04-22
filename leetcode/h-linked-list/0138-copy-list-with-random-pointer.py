"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from _toolbox.LinkedListFactory import LinkedListFactory
from _toolbox.LinkedList import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        current = head

        while current:
            old_to_new[current] = Node(current.val, None, None)
            current = current.next

        current = head

        while current:
            if current.next is not None:
                old_to_new[current].next = old_to_new[current.next]

            if current.random is not None:
                old_to_new[current].random = old_to_new[current.random]

            current = current.next

        return old_to_new[head]

solution = Solution()

head = LinkedListFactory.array_with_random_to_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
result = solution.copyRandomList(head)

print("pass") if LinkedListFactory.linked_list_to_array_with_random(result) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]  else print("fail")
