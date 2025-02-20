def deduplicate_lists(lst1, lst2, reverse=False):
    new_list = lst1 + lst2
    new_list = set(new_list)
    new_list = list(new_list)
    return sorted(new_list, reverse=reverse)
