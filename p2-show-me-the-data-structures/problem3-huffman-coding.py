import sys


class Node:

    def __init__(self, char, frequency):
        self.left = None
        self.right = None
        self.char = char
        self.frequency = frequency

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_value(self):
        return self.char


class Tree:

    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def pre_order(self):
        visit_order = list()

        def traverse(node):
            if node:
                # visit the node
                visit_order.append(node.get_value())

                # traverse left subtree
                traverse(node.get_left_child())

                # traverse right subtree
                traverse(node.get_right_child())

        traverse(self.root)

        return visit_order

    def path_from_root_to_node(self, root, char):
        """
        Assuming data as input to find the node
        The solution can be easily changed to find a node instead of data
        :param data:
        :return:
        """
        output = self.path_from_node_to_root(root, char)
        return list(reversed(output))

    def path_from_node_to_root(self, root, char):
        if root is None:
            return None

        elif root.char == char:
            return [char]

        left_answer = self.path_from_node_to_root(root.left, char)
        if left_answer is not None:
            # left_answer.append(root.char)
            left_answer.append('0')
            return left_answer

        right_answer = self.path_from_node_to_root(root.right, char)
        if right_answer is not None:
            # right_answer.append(root.char)
            right_answer.append('1')
            return right_answer
        return None


class Huffman:

    @staticmethod
    def encode(data):

        frequency_count = Huffman.__count_frequency(data)

        huffman_tree = Huffman.__build_tree(frequency_count)

        encoded_data = ''

        for char in data:
            path = huffman_tree.path_from_root_to_node(huffman_tree.get_root(), char)

            encoded_char = "".join(path[:-1])

            encoded_data = encoded_data + encoded_char

        return encoded_data, huffman_tree

    @staticmethod
    def decode(data, tree):

        if tree is None:
            return ''

        decoded_data = ''

        node = tree.get_root()

        for bit in data:

            if bit == '0':
                node = node.left
                if (node.get_left_child() is None) and (node.get_right_child() is None):
                    decoded_data = decoded_data + node.char
                    node = tree.get_root()

            if bit == '1':
                node = node.right
                if (node.get_left_child() is None) and (node.get_right_child() is None):
                    decoded_data = decoded_data + node.char
                    node = tree.get_root()

        return decoded_data

    @staticmethod
    def __count_frequency(data):

        frequency_count = {}

        for char in data:
            if char in frequency_count:
                frequency_count[char] += 1
            else:
                frequency_count[char] = 1

        return frequency_count

    @staticmethod
    def __build_tree(frequency_count):

        from queue import PriorityQueue

        q = PriorityQueue()

        for char in frequency_count.keys():
            node = Node(char=char, frequency=frequency_count[char])
            count = frequency_count[char]
            q.put((count, char, node))

        huffman_tree = None

        while not q.empty():
            cnt, chr1, node1 = q.get()

            if not q.empty():
                cnt, chr2, node2 = q.get()
                new_node = Node(chr1+chr2, node1.frequency + node2.frequency)
                new_node.left = node1
                new_node.right = node2

                q.put((node1.frequency + node2.frequency, new_node.char, new_node))
            else:
                huffman_tree = Tree(node1)
                break

        return huffman_tree


def test_encode_message():

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman.encode(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman.decode(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print("Pass: Decoded message is the same as original." if decoded_data == a_great_sentence else "Fail")


def test_encode_empty_message():

    a_great_sentence = ""

    encoded_data, tree = Huffman.encode(a_great_sentence)
    decoded_data = Huffman.decode(encoded_data, tree)

    print("Pass: Decoded message is the same as original." if decoded_data == a_great_sentence else "Fail")


def test_encode_large_message():

    a_great_sentence = "Huffman coding uses a specific method for choosing the representation for each symbol, " \
                       "resulting in a prefix code (sometimes called prefix-free codes, that is, the bit string " \
                       "representing some particular symbol is never a prefix of the bit string representing any " \
                       "other symbol). Huffman coding is such a widespread method for creating prefix codes that the " \
                       "term Huffman code is widely used as a synonym for prefix code even when such a code is not " \
                       "produced by Huffman's algorithm. "

    encoded_data, tree = Huffman.encode(a_great_sentence)
    decoded_data = Huffman.decode(encoded_data, tree)

    print("Pass: Decoded message is the same as original." if decoded_data == a_great_sentence else "Fail")


if __name__ == "__main__":
    test_encode_message()
    test_encode_empty_message()
    test_encode_large_message()
