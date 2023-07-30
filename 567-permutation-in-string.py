class Solution:

    def scan(self, s):
        dict = {}

        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1

        return dict

    def scanWindow(self, s, p1, p2):
        dict = {}

        for i in range(p1, p2):
            c = s[i]
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1

        return dict

    def scanWindowOptimised(self, s, p1, p2, w_dict, lng):

        c = s[p2]

        if c in w_dict:
            w_dict[c] += 1
        else:
            w_dict[c] = 1

        if p2 - p1 == lng:
            cr = s[p1]
            w_dict[cr] -= 1

            if w_dict[cr] == 0:
               del w_dict[cr]

    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = self.scan(s1)
        w_dict = {}

        assert self.scan("ab") == self.scan("ab")
        assert self.scan("ab") != self.scan("abc")

        p1 = p2 = 0

        while p2 < len(s2):
            self.scanWindowOptimised(s2, p1, p2, w_dict, len(s1))

            p2 += 1

            if p2 > len(s1):
                p1 += 1


            if w_dict == s1_dict:
                return True

        return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #
    #     s1_dict = self.scan("ab")
    #
    #     assert self.scan("ab") == self.scan("ab")
    #     assert self.scan("ab") != self.scan("abc")
    #
    #     p1 = 0
    #     p2 = len(s1)
    #
    #     while p2 < len(s2):
    #         p1 += 1
    #         p2 += 1
    #
    #         w_dict = self.scanWindow(s2, p1, p2)
    #
    #         if w_dict == s1_dict:
    #             return True
    #
    #     return False

solution = Solution()
print("pass") if solution.checkInclusion("ab", "eidbaooo") == True else print("fail")
print("pass") if solution.checkInclusion("ab", "eidboaoo") == False else print("fail")
print("pass") if solution.checkInclusion("ab", "eioaoab") == True else print("fail")
print("pass") if solution.checkInclusion("a", "ab") == True else print("fail")
