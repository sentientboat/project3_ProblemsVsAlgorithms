This script works by trying to square each integer, starting at 0, and stopping
once we find an integer that gives a result greater than the input. At that point
we know that the previous int was the desired solution.

By definition, this is time complexity O(log(n)). O(log(n))+1, to be precise.
Space complexity is O(1), which will vary a bit depending on the length of the
involved numbers.

I also added clauses to  ignore null values, and set an optional maximum size to
deal with potentially too big numbers. The default for this is 9999800001, which results
from 99999^2 ( I arbitrarily decided that the while loop would stop before having
to square numbers with length 6).
I also left in the option to ignore max values and just let the computer run forever
in case someone needs that.
