from route_planner import RoutePlanner
from helpers import load_map
from helpers import show_map


def test_route_planer():
    map_10 = load_map('map-10.pickle')
    show_map(map_10)

    map_40 = load_map('map-40.pickle')
    show_map(map_40)

    planner = RoutePlanner(map_40)
    path = planner.find_shortest_path(start=5, goal=34)

    if path == [5, 16, 37, 12, 34]:
        print("great! Your code works for these inputs!")
    else:
        print("something is off, your code produced the following:")
        print(path)


def test_route_planer_multiple_paths():
    from tester import test
    from student_code import shortest_path
    test(shortest_path)


if __name__ == "__main__":
    test_route_planer()
    test_route_planer_multiple_paths()
