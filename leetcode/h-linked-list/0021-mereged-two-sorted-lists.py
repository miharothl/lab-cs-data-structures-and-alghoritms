# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next

            tail = tail.next

        tail.next = list1 or list2

        return dummy.next


def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])

    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def get_linked_list_values(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


solution = Solution()

list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,4])
print('pass') if get_linked_list_values(solution.mergeTwoLists(list1, list2)) == [1,1,2,3,4,4] else print('fail')

list1 = build_linked_list([])
list2 = build_linked_list([])
print('pass') if get_linked_list_values(solution.mergeTwoLists(list1, list2)) == [] else print('fail')

"""
Idea:
* create dummy
* create tail set it to dummy.next
* iterate through nodes using while list1 and list2
** point smaller node to tail.next
** move tail to next
** move list to next
* append the remaining node to tail.next
* return dummy next 

Time:
O(N+M), N is length of linked list 1 and M is length of linked list 2

Space:
O(1) - in place 
"""
