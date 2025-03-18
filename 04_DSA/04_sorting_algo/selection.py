def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        # Assume the current index is the smallest
        smallest_idx = i
        # Check the rest of the list for a smaller element
        for j in range(i + 1, n):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        # Swap the current element with the smallest found element
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
