def counting_sort(input):
    counter = [0 for x in range(10)]
    for i in input:
        counter[i] +=1
    r = 9
    while r >= 0:
        while counter[r] > 0:
            yield(r)
            counter[r] -= 1
        r -= 1


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

    #items = counting_sort(input_list)
    num1 = ""
    num2 = ""
    num_pointer = 1
    for item in counting_sort(input_list):
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
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

print("\nTest Case 1: empty list. Should print an error and return none")
print(rearrange_digits([]))

print("\nTest Case 2: list with invalid input. Should print an error and return none")
print(rearrange_digits([1,5,6,3,5.3]))

print("\nTest Case 3: list with two digit integers. Should print an error and return none")
print(rearrange_digits([1,2,3,4,5,50]))
