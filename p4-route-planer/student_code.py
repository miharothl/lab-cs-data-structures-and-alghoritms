from route_planner import RoutePlanner


def shortest_path(M, start, goal):
    planner = RoutePlanner(M)
    return planner.find_shortest_path(start=start, goal=goal)
