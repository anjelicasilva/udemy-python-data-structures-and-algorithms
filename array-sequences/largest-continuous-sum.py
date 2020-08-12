# Given an array of integers (positive and negative)
# find the largest continuous sum.

def large_cont_sum(arr): 

    largest_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > largest_sum:
            largest_sum = current_sum
    return largest_sum


# Solution

def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum 