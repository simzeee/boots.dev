def sort_dates(dates):
    sorted_dates = sorted(dates, key=transform_date)
    return sorted_dates


def transform_date(date):
    month, day, year = map(int, date.split("-"))
    return (year, month, day)
