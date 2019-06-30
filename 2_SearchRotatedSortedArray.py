
def rotated_array_search(input_list, number, left=0):
    if len(input_list) == 0:
        return(-1)
    if len(input_list) == 1 and input_list[0] != number:
        return(-1)
    center = (len(input_list)-1) // 2

    if input_list[center] == number:
        return center + left

    # check if items to be checked are valid
    if not isinstance(input_list[center+1], int):
        print("Error, input list has non-int entries")
        return(-1)
    if not isinstance(input_list[-1], int):
        print("Error, input list has non-int entries")
        return(-1)

    if number >= input_list[center+1] and number <= input_list[-1]:
        return rotated_array_search(input_list[center+1:], number, left+center+1)
    elif number >= input_list[center+1] and input_list[center+1] > input_list[-1]:
        return rotated_array_search(input_list[center+1:], number, left+center+1)
    else:
        return rotated_array_search(input_list[:center], number, left)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        print("Expected {}".format(linear_search(input_list, number)))
        print("Got {}".format(rotated_array_search(input_list, number)))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge case 1: empty list (returns -1)
print(rotated_array_search([], 10))

# Edge case 2: null target number (returns -1)
print(rotated_array_search([], 10))

# Edge case 2: null target number (returns -1 and prints an error)
print(rotated_array_search([6, 7, 8, 1, [2, 1], 3, 4], 10))
