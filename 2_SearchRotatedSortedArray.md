This script is a simple binary search with some extra clauses to deal with the rotation.
For this, I will use a modified version of the binary search algorithm we wrote
in lesson 1.

Overall this has too many ifs and elses, which is not that elegant. Anyhow, this
is the best I could think of, and since the whole thing is basically a binary
search function time complexity is still O(log(n)) where n is the length of the list.

I added some ifs to check if the items that need to be checked from the input list
are all integers. This prints a message to the console if something other than an int is found.
However, this only detects elements that are relevant to the function. Otherwise
I would have had to parse the entire list to check it's integrity, and that would mean
adding O(n) complexity.
Space complexity is O(log(n)) too, since slicing lists produces additional lists,
each one taking O(n) space. And since the deeper we go into recursion the shorter
these lists get, overall space complexity resolves to O(log(n))
