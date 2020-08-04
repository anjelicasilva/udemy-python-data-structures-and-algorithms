# Given an array of integers (positive and negative) find the largest continuous sum.

def large_cont_sum(arr): 

    largest_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > largest_sum:
            largest_sum = current_sum
    return largest_sum
