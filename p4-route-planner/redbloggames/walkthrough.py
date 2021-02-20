from implementation import *


################################################################################
# BFS
def breadth_first_search(graph: Graph, start: Location):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    reached: Dict[Location, bool] = {}
    reached[start] = True

    while not frontier.empty():
        current: Location = frontier.get()
        print("  Visiting %s" % current)
        for next in graph.neighbors(current):
            if next not in reached:
                frontier.put(next)
                reached[next] = True


print('Reachable from A:')
breadth_first_search(example_graph, 'A')
print('Reachable from E:')
breadth_first_search(example_graph, 'E')




################################################################################
# draw
from implementation import *
g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
draw_grid(g)

################################################################################
# dijkstra
from implementation import *
start, goal = (1, 4), (8, 3)
came_from, cost_so_far = dijkstra_search(diagram4, start, goal)
draw_grid(diagram4, number=cost_so_far, start=start, goal=goal)

################################################################################
# a-star
from implementation import *
start, goal = (1, 4), (8, 3)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, path=reconstruct_path(came_from, start=start, goal=goal))

i = 1