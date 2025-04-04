#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime 
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print("Current day:", day)
print("Current month:", month)
print("Current year:", year)
print("Current hour:", hour)
print("Current minute:", minute)
print("Current timestamp:", timestamp)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

#Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
time = datetime.strptime(time_string, "%d %B, %Y")
print("Time object:", time)

#Calculate the time difference between now and new year.
new_year = datetime(year + 1, 1, 1)
difference = new_year - now
print("Time difference between now and new year:", difference)

#Calculate the time difference between 1 January 1970 and now.
time0 = datetime(1970, 1, 1)
difference = now - time0
print("Time difference between 1 January 1970 and now:", difference)

#Think, what can you use the datetime module for? Examples:
#Time series analysis
#To get a timestamp of any activities in an application
#Adding posts on a blog
from datetime import datetime
series = [datetime(2023, 1, 1),
    datetime(2023, 2, 1),
    datetime(2023, 3, 1),
    datetime(2023, 4, 1),
    datetime(2023, 5, 1)]
for date in series:
    print(date.strftime("%Y-%m-%d"))

