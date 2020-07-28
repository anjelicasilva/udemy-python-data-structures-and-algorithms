def pair_sum(num_list, k):
    count = 0
    for idx, num in enumerate(num_list):
        while idx < len(num_list):
            idx = idx + 1
            if num + num_list[idx] == k:
                count += 1
    return count




