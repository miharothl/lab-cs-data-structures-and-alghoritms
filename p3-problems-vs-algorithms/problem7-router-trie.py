# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.path_segments = {}

    def insert(self, path_segment):
        # Insert the node as before
        if path_segment not in self.path_segments.keys():
            self.path_segments[path_segment] = RouteTrieNode(None)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler=handler)
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, path_segments: str, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for path_segment in path_segments:
            node.insert(path_segment)
            node = node.path_segments[path_segment]

        node.handler = handler

    def find(self, path_segments):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root

        for path_segment in path_segments:
            if path_segment not in node.path_segments:
                return None

            node = node.path_segments[path_segment]

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        path_sections = self.split_path(path)
        self.router.insert(path_sections, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        path_sections = self.split_path(path)
        handler = self.router.find(path_sections)
        return handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return [path_section for path_section in path.split("/") if path_section]


def test_router(debug=False):
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    # router = Router("root handler")

    root_handler = 'root handler'
    about_handler = 'about handler'

    router = Router(root_handler)
    router.add_handler("/home/about", about_handler)  # add a route

    # some lookups with the expected output
    handler = router.lookup('/')
    if debug:
        print(handler)  # should print 'root handler'
    print('Pass') if handler == root_handler else print('Fail')

    handler = router.lookup('/home')
    if debug:
        print(handler)  # should print None
    print('Pass') if handler is None else print('Fail')

    handler = router.lookup('/home/about')
    if debug:
        print(handler)  # should print 'about handler'
    print('Pass') if handler == about_handler else print('Fail')

    handler = router.lookup('/home/about/')
    if debug:
        print(handler)  # should print 'about handler'
    print('Pass') if handler == about_handler else print('Fail')

    handler = router.lookup('/home/about/me')
    if debug:
        print(handler)  # should print None
    print('Pass') if handler is None else print('Fail')


def test_router_edge_conditions():
    root_handler = None
    about_handler = None

    router = Router(root_handler)
    router.add_handler("/home/about", about_handler)  # add a route

    # some lookups with the expected output
    handler = router.lookup('/')
    print('Pass') if handler == root_handler else print('Fail')


def test_router_long_path():
    root_handler = 'root handler'
    large_handler = 'large_handler'

    long_path = "/this/is/long/path/longer/then/tested/before/lets/see/if/it/works/this/is/long/path/longer/then" \
                "/tested/before/lets/see/if/it/works "

    router = Router(root_handler)
    router.add_handler(long_path, large_handler)  # add a route
    router.add_handler(long_path, large_handler)  # add a route twice should work as well

    # some lookups with the expected output
    handler = router.lookup(long_path)
    print('Pass') if handler == large_handler else print('Fail')


if __name__ == "__main__":
    test_router(debug=True)
    test_router_edge_conditions()
    test_router_long_path()
