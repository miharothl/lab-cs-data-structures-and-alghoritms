# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(n):
    firstBad = 100

    if n < firstBad:
        return False
    else:
        return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1 = 0
        p2 = n
        return self.firstBadVersionRecursive(n, p1, p2)

    def firstBadVersionRecursive(self, n, p1, p2):

        if p1 == p2:
            return p1

        mid = (p1 + p2) // 2

        if not isBadVersion(mid):
            p1 = mid + 1

        if isBadVersion(mid):
            p2 = mid

        return self.firstBadVersionRecursive(n, p1, p2)


solution = Solution()
print(solution.firstBadVersion(1000))

