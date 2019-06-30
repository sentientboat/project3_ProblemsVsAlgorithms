def get_min_max(ints):
    if len(ints) == 0:
        print("Can't find max and min of an empty list")
        return(())
    min = ints[0]
    max = ints[0]
    for i in ints:
        if not isinstance(i, int):
            if isinstance(i, float):
                print("Found float values, will be rounded down")
                i = int(i)
            else:
                print("Can't sort non-int objects, found {} instead".format(
                    type(i)))
                return(())
        if i > max:
            max = i
        if i < min:
            min = i
    return((min,max))

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

#Test case 1: empty list (returns an empty tuple and prints a message to the console)
print(get_min_max([]))

# Test case 2: list with invalid inputs (raises error, return empty tuple)
l = [i for i in range(15)]
l[4] = None
print(get_min_max(l))

# Test case 3: list with float inputs (raises warnings but works anyway)
l = [i for i in range(15)]
l[4] = 55.63
l[8] = -5698.9
print(get_min_max(l))
