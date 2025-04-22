# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        r = reversed(s)

        sum = 0
        prev_value = 0
        for c in r:
            current = roman[c]

            if current >= prev_value:
                sum += current
            else:
                sum -= current

            prev_value = current

        return sum

        # def convertOne(c: chr):
        #
        #     if c == "M":
        #         return 1000
        #     elif c == "D":
        #         return 500
        #     elif c == "C":
        #         return 100
        #     elif c == "L":
        #         return 50
        #     elif c == "X":
        #         return 10
        #     elif c == "V":
        #         return 5
        #     elif c == "I":
        #         return 1
        #
        #
        # sum = 0
        #
        # for i in range(len(s)):
        #     subtract = False
        #
        #     c = s[i]
        #
        #     if i<len(s)-1:
        #         nc = s[i+1]
        #         if convertOne(nc) > convertOne(c):
        #             subtract = True
        #
        #     if subtract:
        #         sum -= convertOne(c)
        #     else:
        #         sum += convertOne(c)
        #
        # return sum

solution = Solution()

s = "III"
print("pass") if solution.romanToInt(s) == 3 else print("fail")

s = "LVIII"
print("pass") if solution.romanToInt(s) == 58 else print("fail")

s = "MCMXCIV"
print("pass") if solution.romanToInt(s) == 1994 else print("fail")


"""
Idea:
* use hashtable for mapping
* reverse string to avoid look ahead
* traverse the string,
** using the prev_value determine if you need to add or subtract

Time:
O(n) - one pass through the string, one for reversal

Space:
O(1) - couple additional data structures, all limited in size
"""