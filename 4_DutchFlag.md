This is basically the same as the sorting problem in "lesson 2: Sorting algorithms"
I basically copied the solution to that exercice and added a return clause so the
test function works.

Just because, I added a clause that exits the function and returns an error if
values other than 0,1 or 2 are found.

This sorts the list in a single traversal, by putting each zero at the start of
the array, each 2 at the end, and assuming that everything else are 1s.

Time complexity is O(n) since we check every item in the list once.
Space complexity is O(1) since we sort the list in place.
