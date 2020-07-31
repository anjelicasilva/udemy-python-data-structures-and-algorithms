def finder(arr1, arr2):
    num_dict = {}
    for num in arr2:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    for number in arr1:
        if number in num_dict and num_dict[number] != 0:
            num_dict[number] -= 1
        else:
            return number

# Solution

def finder(arr1,arr2):
    # Sort the arrays
    arr1.sort()
    arr2.sort()
    
    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    
    # Otherwise return last element
    return arr1[-1]