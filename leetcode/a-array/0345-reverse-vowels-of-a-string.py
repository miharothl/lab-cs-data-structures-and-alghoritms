# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:

    def is_vowel(self, char: str) -> bool:
        char = char.lower()

        vowels = ['a', 'e', 'i', 'o', 'u']

        if char in vowels:
            return True

        return False

    def reverseVowels(self, s: str) -> str:

        s_list = list(s)

        p0 = 0
        p1 = len(s) - 1

        while p0 < p1:

            if not solution.is_vowel(s_list[p0]):
                p0 += 1
            else:

                if not self.is_vowel(s_list[p1]):
                    p1 -= 1
                else:
                    char = s_list[p0]
                    s_list[p0] = s_list[p1]
                    s_list[p1] = char

                    p0 += 1
                    p1 -= 1

        return ''.join(s_list)


solution = Solution()
solution.reverseVowels("hello")


solution.is_vowel('a')

print("Pass") if solution.reverseVowels("hello") == "holle" else print("Fail")
print("Pass") if solution.reverseVowels("leetcode") == "leotcede" else print("Fail")
