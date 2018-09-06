## 1. First Challenge (Simple) - To spot patterns and create regular experessions: ##
# Determined a regular expression that's four characters long and matches every string in the list strings and assigned it to the variable regex.

strings = ["data science", "big data", "metadata"]
regex = "data"



## 2. Wildcards in Regular Expressions ## 
# Using special character '.' and assigning a regular expression that is three characters long and matches every string in strings to the variable regex.

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"



## 3. Searching the Beginnings And Endings Of Strings ## 
# Using special character '^' to assign a regular expression that's seven characters long and matches every string in strings (except for bad_string) to the variable regex.

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b....r"




""" About our dataset that is used starting from the next section:

Reddit is a content and community website where users can submit links, text posts, and other types of content to groups of people with similar interests. These groups are called subreddits, and each one specializes in a particular topic. For example, AskReddit is a popular subreddit where you can pose questions to the entire Reddit community. Users answer the questions by commenting on them.

In the next section, we'll be working with a data set containing the top 1,000 questions users posted to AskReddit in 2015. Reddit user P_S_Laplace created the data set, which has five columns that appear in the following order:

Title -- The title of the post
Score -- The number of upvotes the post received
Time -- When the post was posted
Gold -- How much Reddit Gold users gave the post
NumComs -- The number of comments the post received
"""



## 5. Reading and Printing our datafile, "askreddit_2015.csv" ##

import csv

# Reading in data from the dataset

f = open("askreddit_2015.csv","r")
posts_with_header = list(csv.reader(f))
posts = posts_with_header[1:]  # creating a dataset without the header row

# Printing the dataset

for post in posts[:10]:
    print (post)




## 6. Counting Simple Matches in the Data Set with re() ##
# Using re.search() function from the "re module" to Count the number of posts in our data set that match the regex "of Reddit" 
# and assigning the count to of_reddit_count.

import re

of_reddit_count = 0

for post in posts:
        if re.search("of Reddit",post[0]) is not None:
            of_reddit_count += 1
#            print ("Post:", post [0])
#            print ("post number:", of_reddit_count)
print ("No of posts with 'of Reddit' in the title: ", of_reddit_count)




## 7. Using Square Brackets to Match Multiple Characters ##
# Using square bracket notation to make the code account for both capitalizations of "Reddit", 
# and counting how many posts contain "of Reddit" or "of reddit" in the title.
# and assigning the resulting count to of_reddit_count.

import re

of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1



## 8. Escaping Special Characters ##
# Escaping the square bracket characters to count the number of posts in our data set that contain the "[Serious]" tag
# and Assigning the count to serious_count.
import re

serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count += 1



## 9. Combining Escaped Characters and Multiple Matches ##
# Refining the code to count how many posts have either "[Serious]" or "[serious]" in the title.
# Assigning the count to serious_count.

import re

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1




## 10. Adding More Complexity to our Regular Expression ##
# Refining the code so that it counts how many posts have the serious tag enclosed in either square brackets or parentheses.
# Assigning the count to serious_count.

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_count += 1




## 11. Combining Multiple Regular Expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

# Using the "^" character to count how many posts include the serious tag at the beginning of the title
# and assigning this count to serious_start_count.
for row in posts:
    if re.search("^[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_start_count += 1
        
# Using the "$" character to count how many posts include the serious tag at the end of the title
# and assigning this count to serious_end_count.
for row in posts:
    if re.search("[\[\(][Ss]erious[\)\]]$", row[0]) is not None:
        serious_end_count += 1

# Using the "|" character to count how many posts include the serious tag at either the beginning or end of the title
# and assigning this count to serious_count_final.
for row in posts:
    if re.search("^[\[\(][Ss]erious[\)\]]|[\[\(][Ss]erious[\)\]]$", row[0]) is not None:
        serious_count_final += 1




# We've looked at one way we can account for inconsistencies in data; now let's examine another approach.




## 12. Using Regular Expressions to Substitute Strings ##
# Replacing "[serious]", "(Serious)", and "(serious)" with "[Serious]" for all of the titles in posts.

import re
for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious[\]\)]","[Serious]", row[0])
       




## 13. Matching Years with Regular Expressions ##

# "strings" variable used below contains a number of strings.

import re

year_strings = []

# Looping through strings and using re.search() to determine whether each string contains a year between 1000 and 2999
# and storing every string that contains a year in year_strings using the " .append()" function
for string in strings:
    if re.search("[1-2][0-9][0-9][0-9]",string) is not None:
                year_strings.append(string)
        




## 14. Repeating Characters in Regular Expressions ##
# Using a regex that takes advantage of curly brackets

import re

year_strings = []

for string in strings:
    if re.search("[1-2][0-9]{3}",string) is not None:
                year_strings.append(string)

## 15. Challenge: Extracting all Years ##
# Using re.findall() to generate a list of all years between 1000 and 2999 in the string "years_string"
# and assigning the result to years

import re
years_string  = "2015 was a good year, but 2016 will be better!"
years = re.findall("[1-2][0-9]{3}", years_string)