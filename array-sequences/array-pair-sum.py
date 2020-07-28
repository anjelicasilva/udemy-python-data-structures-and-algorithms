def pair_sum(num_list, k):
    count = 0
    for idx, num in enumerate(num_list):
        while idx < len(num_list):
            idx = idx + 1
            if num + num_list[idx] == k:
                count += 1
    return count


def pair_sum_solution(arr, k):
    #Edge Case
    if len(arr) < 2:
        return
    
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target)), max((num, target)) )
        
    return len(output)



