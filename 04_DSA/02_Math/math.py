from statistics import mean


def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    return mean(audiences_followers) * (len(audiences_followers) ** 1.2)


def get_follower_prediction(follower_count, influencer_type, num_months):
    r = 2
    if influencer_type == "fitness":
        r = 4
    if influencer_type == "cosmetic":
        r = 3
    return follower_count * r**num_months


import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


def num_possible_orders(num_posts):
    result = 1
    count = 1
    while count <= num_posts:
        result *= count
        count += 1
    return result
