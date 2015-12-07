import time

def februar_gap(year):
    if year % 4:
        return 0
    
    if year %100:
        return 1
    
    if year % 400:
        return 0
    return 1
def day_gap(year, month):
    if month ==2:
        return februar_gap(year)
    if month in [4, 6, 9, 11]:
        return 2
    return 3
    
def count_sundays_first_of_month():
    d = 2 #1st januar of 1900 was monday, so 1st januar of 1901 is tuesday
    count = 0
    for year in range(1901,2001):
        for month in range(1,13):
            d = (d + day_gap(year, month))%7
            if d == 0:
                count = count + 1
    return count
          
    