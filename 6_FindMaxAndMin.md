This should be a trivial problem: just parse the input list, check every item
against the current max and min values, and  update those when necessary.
The most important concept would perhaps be initializing the max and min values
to values in the array instead of some arbitrary number.

Since we parse the list only once, time complexity is O(n) and  space complexity
is O(1) since we would always only need a couple of extra variables (max and min)

Added some extra clauses to deal with invalid inputs and empty inputs too.
