def find_minimum(nums):
    minimum = float("inf")
    if not nums:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


from functools import reduce


def sum(nums):
    if not nums:
        return 0
    sum = reduce(lambda x, y: x + y, nums)
    return sum
