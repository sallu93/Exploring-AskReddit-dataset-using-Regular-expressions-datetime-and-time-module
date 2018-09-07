## 1. The Time Module ##

# Retrieving the current Unix timestamp using the time.time() function.
# Returning the current timestamp and assigning it to current_time.
# and displaying current_time

import time
current_time = time.time()
print (current_time)




## 2. Converting Timestamps ##

# Using the time.time() function to assign the current Unix timestamp to a new variable current_time.
# Converting current_time to a struct_time object and assigning the resulting object to current_struct_time.
# Assigning the current hour to current_hour and displaying the value.

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)





## 3. The datetime module ##

# Importing the datetime module.
# Assigning the datetime object representation of the current time to a new variable current_datetime.
# Assigning the current year to current_year.
# Assigning the current month to current_month.

import datetime

current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month





## 4. Timedelta ##

# Creating an instance of the datetime class that represents the day March 22, 2233. Assigning this to a new variable kirks_birthday.
# Creating an instance of the timedelta class representing 15 weeks and assigning to diff.
# Finding the date 15 weeks prior to March 22, 2233 and assigning the resulting datetime instance to before_kirk.

import datetime
kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff





## 5. Formatting Dates ##

# Using the datetime.datetime.strftime() method to display mystery_date, a datetime instance already created, in the following format:
# [12-hour time][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year]
# Here's an example in that format: "11:00AM on Wednesday March 03, 2010"
# mystery_date:  2015-12-31 00:00:00 (This instance was already created in my learning platform. Please create the instance before using the below code )
# Storing this string in the new variable mystery_date_formatted_string and displaying it.




import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print (mystery_date_formatted_string)

# For more options, Can refer to the documentation for the strftime() method using the below link, which provides a useful summary table of the different options.
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior






## 6. Parsing Dates ##

# The datetime.datetime.strptime() function allows us to convert a string to a datetime instance. The reverse of the previous bit of code.

import datetime
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print (mystery_date_2)





## 7. ABOUT OUR DATASET ##

# The AskReddit data has been read into the posts variable as a list of lists in the code below.

import csv
f = open("askreddit_2015.csv","r")
posts_with_header = list(csv.reader(f))
posts = posts_with_header[1:]  # creating a dataset without the header row

# Each nested list represents an AskReddit post. 
# Here's what the first three lists in posts looks like: 
""" posts = [
            ['What\'s your internet "white whale", something you\'ve been searching for years to find with no luck?', '11510', '1433213314.0', '1', '26195'],
            ["What's your favorite video that is 10 seconds or less?", '8656', '1434205517.0', '4', '8479'],
            ['What are some interesting tests you can take to find out about yourself?', '8480', '1443409636.0', '1', '4055'],
            ...
        ]
"""




## 8. Reformatting Our Data ##

# You can see that the values in the Time column are formatted as Unix timestamps, not human-readable strings.
# We'll be converting the Unix timestamp for each row to a datetime object using datetime.datetime.fromtimestamp() 
# and store the result back in the row, replacing the Unix timestamp.




import datetime
for row in posts:
    row[2] = float(row[2])
    row[2] = datetime.datetime.fromtimestamp(row[2])






## 9. Counting Posts from March ##

# Looping through posts, and for each row:
# Using the datetime.month attribute to check if the datetime instance at index 2 equals 3.
# If so, incrementing march_count.

march_count = 0
for row in posts:
    if row[2].month == 3:
        march_count += 1





## 10. Counting Posts from Any Month ##
        
# Creating a function that takes in an integer value representing a month, and returns the number of posts users submitted during that month.
# Testing the function for the month of February and August.


def posts_count(month):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = posts_count(2)
aug_count = posts_count(8)

