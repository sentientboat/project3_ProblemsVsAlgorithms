# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root):
        # Initialize the trie with an root node and a handler,
        # this is the root path or home page node.
        self.root = RouteTrieNode()
        self.root.handler = root

    def insert(self, split_path, handler):
        node = self.root
        for section in split_path:
            node.insert(section)
            node = node.children[section]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for section in path:
            if section in node.children:
                node = node.children[section]
            else:
                #print("path not found {}".format(path))
                return(None)
        return(node.handler)

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root, not_found = "Page not found"):
        # Create a new RouteTrie for holding our routes
        self.Trie = RouteTrie(root)
        self.handle_404 = not_found

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Path splitting is delegated to the trie.
        split_path = self.split_path(path)
        self.Trie.insert(split_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        split_path = self.split_path(path)
        result = self.Trie.find(split_path)
        if result is None:
            return(self.handle_404)
        else:
            return(result)

    def split_path(self, path):
        # Handle empty requests
        if len(path) == 0:
            return([])
        # Handle single slash
        if path == "/":
            return([])
        # Handle trailing slashes
        elif path[-1] == '/':
            path = path[:-1]

        return(path.split('/'))

    def path_validator(self, path):
        if path == '/':
            return("")
        if path[-1] == '/':
            return(path[:-1])




# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

#Test case 1: Empty lookup request. Returns the root.
print("\nTest case 1:")
print(router.lookup(""))

#Test case 2: modifying existing nodes
print("\nTest case 2:")
router.add_handler("/home/", "home handler")  # add a route
print(router.lookup("/home")) # should print "home handler"
