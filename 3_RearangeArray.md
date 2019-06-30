The idea here is sorting the list of integers using any method that has
time complexity O(nlog(n)). In this case I've chosen merge sort merely because
I felt like refreshing those lessons.

Once we have a sorted array, we need to build the two output numbers. This is
done by putting the biggest possible digits as much to the left as possible,
and appending the smaller digits to the right.

Building the output numbers has complexity O(n). This would mean that the overall
complexity of this script would be O(n+nlog(n)) which, once simplified, is
still O(nlog(n))

Added some error handling and edge cases.
