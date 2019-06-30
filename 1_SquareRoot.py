def sqrt(number, max_value = 9999800001):
    power = 0
    value = 0
    last_value = 0
    if number is None:
        return("Error, expected a number")

    if number > max_value:
        if max_value == -1:
            pass
        else:
            return("Trying to compute too big a number")

    while power <= number:
        last_value = value
        value +=1
        power = value ** 2

    return(last_value)


    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    pass

# General Test cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Null Test case
print(sqrt(None))
# Should return an error message

# Big int test case
print(sqrt(54484868135303514681351536188616844351231326545745432))
# Should return another error message

# Big int test case
print(sqrt(9999800001))
# Should return 99999

# Big int test case
print(sqrt(9999800002))
# Should return 'too big' error message

# Big int test case
print(sqrt(9999800002, 9999800003))
# Should return 99999
