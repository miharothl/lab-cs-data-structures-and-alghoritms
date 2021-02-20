from math import sqrt
import heapq
from typing import Dict, List, Iterator, Tuple, TypeVar, Optional

T = TypeVar('T')
Location = TypeVar('Location')


class GraphNode(object):
    def __init__(self, val, x, y):
        self.value = val
        self.x = x
        self.y = y
        self.children = []

    def add_child(self, new_node):
        if new_node not in self.children:
            self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


class RoutePlanner:
    def __init__(self, map):
        self.__graph = self.__load_data(map)

    def find_shortest_path(self, start, goal):
        start_node = self.__graph.nodes[start]
        goal_node = self.__graph.nodes[goal]

        found, came_from = self.__a_star_search(start_node, goal_node)
        assert(found == goal_node)
        path = self.__reconstruct_path(came_from, start_node, found)

        return path

    def __a_star_search(self, root_node, goal_node):
        frontier = PriorityQueue()
        frontier.put(root_node, 0)

        came_from: Dict[Location, Optional[Location]] = {}
        cost_so_far: Dict[Location, float] = {}

        came_from[root_node] = None
        cost_so_far[root_node] = 0

        while not frontier.empty():
            current = frontier.get()

            if current.value == goal_node.value:
                return current, came_from

            for next in current.children:
                a = cost_so_far[current]
                b = self.__distance(current, next)
                c = self.__distance(next, goal_node)

                new_cost = a + b

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + c
                    frontier.put(next, priority)
                    came_from[next] = current

        return None, None

    def __closest_child(self, node):
        min_dist = None
        closest = None

        for child in node.children:
            d = self.__distance(node, child)

            if min_dist is None:
                min_dist = d
                closest = child
            else:
                if d < min_dist:
                    min_dist = d
                    closest = child

        return closest

    def __distance(self, node1: GraphNode, node2: GraphNode):
        dx = node2.x - node1.x
        dy = node2.y - node1.y

        d = sqrt(dx*dx + dy*dy)
        return d

    def __load_data(self, M):
        nodes = []

        for key in M.intersections.keys():
            intersection = M.intersections[key]
            node = GraphNode(val=key, x=intersection[0], y=intersection[1])
            nodes.append(node)

        graph = Graph(nodes)
        for i in range(0, len(M.roads)):
            for j in range(0, len(M.roads[i])):
                node_from = nodes[i]
                node_to = nodes[M.roads[i][j]]
                graph.add_edge(node_from, node_to)

        return graph

    def __reconstruct_path(self, came_from: Dict[Location, Location],
                           start: Location, goal: Location) -> List[Location]:
        current: Location = goal
        path: List[Location] = []
        while current != start:
            path.append(current.value)
            current = came_from[current]
        path.append(start.value)  # optional
        path.reverse()  # optional
        return path
