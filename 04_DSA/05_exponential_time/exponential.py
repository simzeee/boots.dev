def fib(n):
    if n == 0:
        return 0
    # For n >= 1, we start with:
    # F(0) = 0, F(1) = 1.
    grandparent = 0
    parent = 1
    # Loop (n - 1) times to compute F(n)
    for _ in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return parent


def power_set(input_set):
    # If the input set is empty, return a list containing an empty list
    if not input_set:
        return [[]]

    # Initialize the final collection of subsets with an empty set
    final_subsets = [[]]

    # For each element in the input list
    for element in input_set:
        new_subsets = []
        # Iterate over each existing subset
        for subset in final_subsets:
            # Create a new subset by adding the current element to the existing subset
            new_subset = subset + [element]
            # Append this new subset to the list of new subsets
            new_subsets.append(new_subset)
        # Extend the main collection of subsets with the newly created subsets
        final_subsets.extend(new_subsets)

    # Return the final collection of subsets
    return final_subsets


# Example usage:
example_set = [1, 2, 3]
print(power_set(example_set))
