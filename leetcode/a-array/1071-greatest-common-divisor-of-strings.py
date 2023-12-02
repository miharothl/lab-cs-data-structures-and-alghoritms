# https://leetcode.com/problems/greatest-common-divisor-of-strings

import math


class Solution:

    # great common string divisor
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        max_length = math.gcd(len(str1), len(str2))

        return str1[:max_length]


solution = Solution()

print("pass") if solution.gcdOfStrings("abcabc", "abc") == "abc" else print("fail")

"""
Problem: gcd of strings
Type: string

Thinking:
* two strings a="abcabc" and b="abc" have common string divisor if
  * a + b = b + a
  * check and return "" if not true
* get max_length of string by calculating gcd(len(a), len(b))
* return substring s1[:max_length]

Complexity:
* Time: 1. we need to compare two strings
          O(M+N) where M and N are string length
        2. calculate gcd using euclidian algorithm https://en.wikipedia.org/wiki/Euclidean_algorithm
          O(log(M*N))
          
        so O(M+N)
* Space:
        compare two strings O(M+N)        
"""
