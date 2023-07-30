
# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        word1_len = len(word1)
        word2_len = len(word2)

        p1 = 0
        p2 = 0

        merged = ""

        for p in range(max(word1_len, word2_len)):

            if p1 < word1_len:
                merged += word1[p1]
                p1 += 1

            if p2 < word2_len:
                merged += word2[p2]
                p2 += 1

        return merged


solution = Solution()
print("pass") if solution.mergeAlternately("abc", "pqr") == "apbqcr" else print("fail")
print("pass") if solution.mergeAlternately("abc", "p") == "apbc" else print("fail")
print("pass") if solution.mergeAlternately("ab", "pqrs") == "apbqrs" else print("fail")
print("pass") if solution.mergeAlternately("", "pqr") == "pqr" else print("fail")
print("pass") if solution.mergeAlternately("abc", "") == "abc" else print("fail")
print("pass") if solution.mergeAlternately("", "") == "" else print("fail")
