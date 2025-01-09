def merge(dict1, dict2):
    merged_dict = {}
    for name in dict1:
        merged_dict[name] = dict1[name]
    for name in dict2:
        merged_dict[name] = dict2[name]
    return merged_dict


def total_score(score_dict):
    score = 0
    for time_period in score_dict:
        score += score_dict[time_period]
    return score
