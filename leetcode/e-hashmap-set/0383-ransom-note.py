# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        letterCount = {}

        for letter in magazine:
            letterCount[letter] = letterCount.get(letter, 0) + 1

        for letter in ransomNote:
            if letterCount.get(letter, 0) == 0:
                return False
            letterCount[letter] -= 1

        return True



"""
Idea:
use hashtable to count letters in magazine

for each letter in ransom letter check if the letter in count hashtable


Time:
O(n+m), where n = len(magazine) and m = len(ransomNote)

Space:
O(1), use hashtable to count letters, which is a bounded set, set with a fixed size

"""



solution = Solution()
ransomNote = "aa"
magazine = "aab"
print("pass") if solution.canConstruct(ransomNote, magazine) == True else print("pass")

ransomNote = "aa"
magazine = "ab"
print("pass") if solution.canConstruct(ransomNote, magazine) == False else print("pass")