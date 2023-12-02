# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero

from collections import defaultdict
from typing import List, Dict


class Solution:

    def __init__(self):
        self.__count = 0

    def createGraph(self, n: int, edges: List[List[int]]) -> Dict:
        graph = defaultdict(list)

        for edge in edges:
            u, v = edge

            graph[u].append((v, 1))
            graph[v].append((u, 0))  # for undirected graph use this

        return graph

    def dfs(self, node, graph, visited):
        # print(node)
        # print(graph[node])

        visited[node] = True

        for neighbour, direction in graph[node]:
            if not visited[neighbour]:

                if direction == 1:
                    self.__count += 1
                    # print('count')
                self.dfs(neighbour, graph, visited)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = self.createGraph(n, connections)

        visited = [False] * n

        self.__count = 0
        self.dfs(0, graph, visited)

        return self.__count


solution = Solution()

n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print("Pass") if solution.minReorder(n, connections) == 3 else print("Fail")

n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
print("Pass") if solution.minReorder(n, connections) == 2 else print("Fail")
