import datetime

# a) Current date and time
current_datetime = datetime.datetime.now()
print("a) Current date and time:", current_datetime)

# b) Current Year
current_year = current_datetime.year
print("b) Current Year:", current_year)

# c) Month of the year
current_month = current_datetime.month
print("c) Month of the year:", current_month)

# d) Week number of the year
week_number = current_datetime.strftime("%U")
print("d) Week number of the year:", week_number)

# e) Weekday of the week
weekday = current_datetime.strftime("%A")
print("e) Weekday of the week:", weekday)

# f) Day of year
day_of_year = current_datetime.timetuple().tm_yday
print("f) Day of year:", day_of_year)

# g) Day of the month
day_of_month = current_datetime.day
print("g) Day of the month:", day_of_month)

# h) Day of week
day_of_week = current_datetime.strftime("%w")
print("h) Day of week:", day_of_week)
