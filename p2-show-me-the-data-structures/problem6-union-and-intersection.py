class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def insert(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def count_nodes_with_same_value(llist, value_counter):
    node = llist.head

    if node is None:
        return

    while node:
        if node.value in value_counter.keys():
            value_counter[node.value] += 1

        else:
            value_counter[node.value] = 1

        node = node.next


def union(llist_1, llist_2):

    value_counter = {}

    count_nodes_with_same_value(llist=llist_1, value_counter=value_counter)
    count_nodes_with_same_value(llist=llist_2, value_counter=value_counter)

    llist = LinkedList()

    for value in value_counter.keys():
        llist.insert(value)

    return llist


def create_set(llist):

    value_counter = {}
    count_nodes_with_same_value(llist=llist, value_counter=value_counter)

    llist_set = LinkedList()

    for value in value_counter.keys():
        llist_set.insert(value)

    return llist_set


def intersection(llist_1, llist_2):

    llist_set_1 = create_set(llist_1)
    llist_set_2 = create_set(llist_2)

    value_counter = {}

    count_nodes_with_same_value(llist=llist_set_1, value_counter=value_counter)
    count_nodes_with_same_value(llist=llist_set_2, value_counter=value_counter)

    llist = LinkedList()

    for value in value_counter.keys():
        if value_counter[value] > 1:
            llist.insert(value)

    return llist


# Test case 1
def test_union_and_intersection_exists():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    or_list = union(linked_list_1, linked_list_2)
    and_list = intersection(linked_list_1, linked_list_2)

    print("Pass: Union contains '{}' nodes. Nodes: '{}'".format(or_list.size(), or_list)
          if or_list.size() == 11 else "Fail")

    print("Pass: Intersection contains '{}' nodes. Nodes: '{}'.".format(and_list.size(), and_list)
          if and_list.size() == 3 else "Fail")


# Test case 2
def test_intersection_not_exist():

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    or_list = union(linked_list_3, linked_list_4)
    and_list = intersection(linked_list_3, linked_list_4)

    print("Pass: Union contains '{}' nodes. Nodes: '{}'".format(or_list.size(), or_list)
          if or_list.size() == 13 else "Fail")

    print("Pass: Intersection contains '{}' nodes. Nodes: '{}'.".format(and_list.size(), and_list)
          if and_list.size() == 0 else "Fail")


# Test case 3
def test_when_linked_list_is_empty():

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    or_list = union(linked_list_3, linked_list_4)
    and_list = intersection(linked_list_3, linked_list_4)

    print("Pass: Union contains '{}' nodes. Nodes: '{}'".format(or_list.size(), or_list)
          if or_list.size() == 7 else "Fail")

    print("Pass: Intersection contains '{}' nodes. Nodes: '{}'.".format(and_list.size(), and_list)
          if and_list.size() == 0 else "Fail")


if __name__ == "__main__":
    test_union_and_intersection_exists()
    test_intersection_not_exist()
    test_when_linked_list_is_empty()
