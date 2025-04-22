from leetcode._toolbox.LinkedList import ListNode, Node


class LinkedListFactory:

    @staticmethod
    def array_to_linked_list(values):
        if not values:
            return None

        head = ListNode(values[0])

        current = head

        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        return head

    @staticmethod
    def linked_list_to_array(head):
        values = []

        while head:
            values.append(head.val)
            head = head.next

        return values

    @staticmethod
    def array_with_random_to_linked_list(data):
        if not data:
            return None

        # Step 1: Create all nodes
        nodes = [Node(val) for val, _ in data]

        # Step 2: Set next pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Step 3: Set random pointers
        for i, (_, rand_index) in enumerate(data):
            if rand_index is not None:
                nodes[i].random = nodes[rand_index]

        return nodes[0]

    @staticmethod
    def linked_list_to_array_with_random(head):
        if not head:
            return []

        index_map = {}  # Node to index mapping
        nodes = []
        current = head
        i = 0
        while current:
            nodes.append(current)
            index_map[current] = i
            current = current.next
            i += 1

        result = []
        for node in nodes:
            rand_index = index_map[node.random] if node.random else None
            result.append([node.val, rand_index])

        return result
