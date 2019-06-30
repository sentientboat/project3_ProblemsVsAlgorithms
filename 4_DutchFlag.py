def sort_012(input_list):
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0
    valid_inputs = {0,1,2}

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        elif input_list[front_index] not in valid_inputs:
            print("Error: found values different than o, 1 or 2")
            return(None)
        else:
            front_index += 1
    return(input_list)


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case: empty list, should return an empty list.
print(sort_012([]))

# Test case: values other than 0, 1 or 2. Should return None and raise error
print(sort_012([0, 0, 2, 3, 2, 1, 1, 1, 2, 0, 2]))

# Test case: Only 1 kind of value. should return a list of 0s
print(sort_012([0 for _ in range(20)]))
