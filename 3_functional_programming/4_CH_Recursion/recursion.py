def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)


def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}

    result = zipmap(keys[1:], values[1:])
    result[keys[0]] = values[0]
    return result


def sum_nested_list(lst):
    total_size = 0
    for item in lst:
        if isinstance(item, int):
            total_size += item
        elif isinstance(item, list):
            total_size += sum_nested_list(item)
    return total_size


def list_files(parent_directory, current_filepath=""):
    file_paths = []
    for key, value in parent_directory.items():
        new_file_path = current_filepath + "/" + key
        if value is None:
            file_paths.append(new_file_path)
        else:
            file_paths.extend(list_files(value, new_file_path))
    return file_paths
