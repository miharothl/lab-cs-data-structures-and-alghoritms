# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        word_to_char= {}
        char_to_word= {}

        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):

            if c in word_to_char:
                if word_to_char[c] != w:
                    return False
            else:
                word_to_char[c] = w

            if w in char_to_word:
                if char_to_word[w] != c:
                    return False
            else:
                char_to_word[w] = c

        return True


solution = Solution()

pattern = "abba"
s = "dog cat cat dog"
print("pass") if solution.wordPattern(pattern, s) == True else print("fail")

pattern = "abba"
s = "dog cat cat fish"
print("pass") if solution.wordPattern(pattern, s) == False else print("fail")


"""
Idea:
* use two hash tables for mapping, s_to_t, t_to_s
* iterate through both arrays using zip
** add mapping s_to_t if not exist, otherwise check if the mapping is the same, if not return False
** add mapping t_to_s if not exist, otherwise check if the mapping is the same, it not return False

Time Complexity:
O(N) - one pass through array

Space Complexity:
O(N) - two hash maps
"""
