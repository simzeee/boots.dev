def find_max(nums):
    return max(nums)


def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if first_name + " " + last_name == full_name:
                return True
    return False


def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)


def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]
    else:
        return None
