# Merge sort
def mergesort(items):
    if len(items) <= 1:
        return(items)

    # Split the lists:
    mid = (len(items))//2
    left = items[:mid]
    right = items[mid:]

    # Split recursively
    left = mergesort(left)
    right = mergesort(right)

    # Merge each list
    return merge(left,right)

def merge(left,right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through either list until one is exhausted
    # Organize the output in decreasing order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Append leftovers
    merged += left[left_index:]
    merged += right[right_index:]

    return(merged)

def rearrange_digits(input_list):
    if len(input_list) == 0:
        print("Error, input list is empy")
        return(None)
    for item in input_list:
        if not isinstance(item, int):
            print("Error: some input items are not be integers")
            return(None)
        if item > 9 or item < 0:
            print("Error: input items should have values between 0 and 9")
            return(None)
    items = mergesort(input_list)
    num1 = ""
    num2 = ""
    num_pointer = 1
    for item in items:
        if num_pointer == 1:
            num1 += str(item)
            num_pointer = 2
        else:
            num2 += str(item)
            num_pointer = 1
    return((int(num1),int(num2)))


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

print("\nTest Case 1: empty list. Should print an error and return none")
print(rearrange_digits([]))

print("\nTest Case 2: list with invalid input. Should print an error and return none")
print(rearrange_digits([1,5,6,3,5.3]))

print("\nTest Case 3: list with two digit integers. Should print an error and return none")
print(rearrange_digits([1,2,3,4,5,50]))
