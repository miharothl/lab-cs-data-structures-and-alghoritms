class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def find_words_recursive(self, node, prefix, words):
        if node.is_word:
            words.append(prefix)

        for char in node.children.keys():
            child = node.children[char]
            self.find_words_recursive(child, prefix+char, words)

    def suffixes(self, suffix=''):
        words = []
        self.find_words_recursive(self, suffix, words)
        return words


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        assert type(prefix) is str

        node = self.root

        for char in prefix:
            if char not in node.children:
                return None

            node = node.children[char]

        return node


def setup_test():
    trie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in wordList:
        trie.insert(word)

    return trie


def test_trie(prefix, expected_suggestions, debug=False):
    trie = setup_test()

    node = trie.find(prefix)
    suggestions = None
    if node:
        suggestions = node.suffixes()

    print('Pass') if suggestions == expected_suggestions else print('Fail')

    if debug:
        print('{} => {}'.format(prefix, suggestions))


def test_trie_edge_conditions():

    trie = Trie()
    try:
        node = trie.find(None)
        print('Fail')
    except AssertionError:
        print('Pass')

    node = trie.find('trie')
    print('Pass') if node is None else print('Fail')




if __name__ == "__main__":
    test_trie('a', ['nt', 'nthology', 'ntagonist', 'ntonym'], debug=True)
    test_trie('anth', ['ology'])
    test_trie('anthr', None)
    test_trie('fu', ["n", "nction"])
    test_trie('x', None)
    test_trie_edge_conditions()



