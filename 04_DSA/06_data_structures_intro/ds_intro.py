def count_marketers(job_titles):
    count = 0
    for word in job_titles:
        if word.lower() == "marketer":
            count += 1
    return count
