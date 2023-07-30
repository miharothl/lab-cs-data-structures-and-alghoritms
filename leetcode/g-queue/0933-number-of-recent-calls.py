# https://leetcode.com/problems/number-of-recent-calls/
from collections import deque

class RecentCounter:

    def __init__(self):

        self.__queue = deque()

    def ping(self, t: int) -> int:

        self.__queue.append(t)

        truncate = t - 3000

        for i in range(len(self.__queue)):

            if self.__queue[0] < truncate:
                self.__queue.popleft()
            else:
                break

        return len(self.__queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


counter = RecentCounter()
print("pass") if counter.ping(1) == 1 else print("fail")
print("pass") if counter.ping(2) == 2 else print("fail")
print("pass") if counter.ping(100) == 3 else print("fail")
print("pass") if counter.ping(3001) == 4 else print("fail")
print("pass") if counter.ping(3002) == 4 else print("fail")

"""
Problem: number of recent calls
Type: queue 

Thinking:
* use queue
* for each ping add to the queue
* calculate bottom threshold
* peak into queue, if less than bottom threshold, deque-popleft
* return len of the queue

Complexity:
* Time: O(N)
* Memory:O(1)
"""
