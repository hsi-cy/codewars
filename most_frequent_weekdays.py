# What is your favourite day of the week? Check if it's 
# the most frequent day of the week in the year.

# You are given a year as integer (e. g. 2001). 
# You should return the most frequent day(s) of the week in that year. 
# The result has to be a list of days sorted by the order of days in week 
# (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). 
# Week starts with Monday.

# Input: Year as an int.

# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

# Preconditions:

# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.

def most_frequent_days(year):
    import datetime 
    # if it's a leap year then there are 366 days and the first three days will be the most 
    # if not a leap year then only the first two
    if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
        # get what is the first day of the year
        day = {'0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday','6':'Sunday'}
        d = datetime.date(year,1,1)
        key = d.weekday()
        if key < 5:
            a = str(key)
            b = str(key+1)
            c = str(key+2)
            ans = [day[a],day[b],day[c]]
            return ans
        elif key == 5:
            a = str(key)
            b = str(key+1)
            c = str(key-6)
            ans = [day[c],day[a],day[b]]
            return ans
        else:
            a = str(key)
            b = str(key-6)
            c = str(key-5)
            ans = [day[b],day[c],day[a]]
        return day[key]
    else:
        # not a leap year
        day = {'0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday','6':'Sunday'}
        d = datetime.date(year,1,1)
        key = d.weekday()
        if key < 6:
            a = str(key)
            b = str(key+1)
            ans = [day[a],day[b]]
            return ans
        else:
            a = str(key)
            b = str(key-6)
            ans = [day[b],day[a]]
            return ans

most_frequent_days(2427)