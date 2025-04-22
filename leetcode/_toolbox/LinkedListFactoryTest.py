import unittest

from _toolbox.LinkedListFactory import LinkedListFactory
from leetcode._toolbox.LinkedList import ListNode, Node


class TestLinkedListFactory(unittest.TestCase):

    def list_nodes_equal(self, node1, node2):
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return node1 is None and node2 is None

    def test_array_to_linked_list_empty(self):
        result = LinkedListFactory.array_to_linked_list([])
        self.assertIsNone(result)

    def test_array_to_linked_list_single_element(self):
        result = LinkedListFactory.array_to_linked_list([42])
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 42)
        self.assertIsNone(result.next)

    def test_array_to_linked_list_multiple_elements(self):
        values = [1, 2, 3, 4]
        result = LinkedListFactory.array_to_linked_list(values)
        expected = ListNode(1)
        current = expected
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        self.assertTrue(self.list_nodes_equal(result, expected))

    def test_linked_list_to_array_empty(self):
        result = LinkedListFactory.linked_list_to_array(None)
        self.assertEqual(result, [])

    def test_linked_list_to_array_single_element(self):
        node = ListNode(99)
        result = LinkedListFactory.linked_list_to_array(node)
        self.assertEqual(result, [99])

    def test_linked_list_to_array_multiple_elements(self):
        node = ListNode(5)
        node.next = ListNode(10)
        node.next.next = ListNode(15)
        result = LinkedListFactory.linked_list_to_array(node)
        self.assertEqual(result, [5, 10, 15])

    def test_round_trip_array_to_linked_list_and_back(self):
        original = [7, 8, 9, 10]
        head = LinkedListFactory.array_to_linked_list(original)
        result = LinkedListFactory.linked_list_to_array(head)
        self.assertEqual(result, original)

    def test_array_with_random_to_linked_list_empty(self):
        result = LinkedListFactory.array_with_random_to_linked_list([])
        self.assertIsNone(result)

    def test_array_with_random_to_linked_list_and_back(self):
        # Format: [value, random_index]
        data = [[10, None], [20, 0], [30, 1]]
        head = LinkedListFactory.array_with_random_to_linked_list(data)
        result = LinkedListFactory.linked_list_to_array_with_random(head)
        self.assertEqual(result, data)

    def test_linked_list_to_array_with_random_none(self):
        # Only node, no random
        node = Node(1)
        result = LinkedListFactory.linked_list_to_array_with_random(node)
        self.assertEqual(result, [[1, None]])

    def test_linked_list_to_array_with_random_self(self):
        # Node points to itself
        node = Node(42)
        node.random = node
        result = LinkedListFactory.linked_list_to_array_with_random(node)
        self.assertEqual(result, [[42, 0]])

    def test_round_trip_array_with_random(self):
        data = [[1, None], [2, 0], [3, 2], [4, 1]]
        head = LinkedListFactory.array_with_random_to_linked_list(data)
        result = LinkedListFactory.linked_list_to_array_with_random(head)
        self.assertEqual(result, data)

if __name__ == "__main__":
    unittest.main()