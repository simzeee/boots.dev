def validate_path(expected_path, character_path):
    name = character_path[0]
    correct = 0
    for i in range(len(character_path) - 1):
        if expected_path[i] == character_path[i + 1]:
            correct += 1
    percentage = float(correct / len(expected_path) * 100)
    return name, percentage
