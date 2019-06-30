I pretty much followed the instructions on the website.
Finding an address should be complexity O(n) where n is the number of sections
in an url. Or, also O(log(n)) if n is the total number of possible addresses.

Space complexity is that of a trie, which is O(log(n))

Added special clauses for "not found" handlers and trailing slashes
