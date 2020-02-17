"""
INSTRUCTIONS

"Herbie's House of Products" is a Massachusetts retail chain with a quality control problem. In fact,
it only sells deceptive, defective, and dangerous items.

Your client is the Massachusetts Danger Rangers, a nonprofit consumer advocate. The Danger Rangers have collected
a list of 1000 members who have purchased worthless items from HHOP and want their money back.
Herbie says that no returns are accepted.

The Danger Rangers want your help preparing Chapter 93A demand letters on behalf of each member.
The information you will need for each member is in the file "member_info.json".
A sample demand letter is in the file "letters/sample_letter.txt".
Each item in the sample demand letter that needs to be customized is marked with <angle brackets>.

## Credits ##

The sample demand letter is inspired by the form letter posted by the Massachusetts Attorney General at
https://www.mass.gov/service-details/30-day-demand-letter

Please follow the sample in letters/sample_letter.txt for your letters in this lab, rather than developing
a new one based on the website.

"""

### STEP ONE ###

# First let's load in the member information from a "JSON" file. This code is provided for you since we haven't
# studied files yet. A JSON file stores integers, strings, and lists in a format similar to the Python variables
# you are already familiar with.

# Here's some code to load the list of Danger Rangers members and the products they bought:



import json

members_file = open('member_info.json')
members = json.load(members_file)
members_file.close()



# Great! Now the `members` variable should contain the same information that you will see if you look inside
# member_info.json. Try printing the `members` variable to make sure, then go on to the next exercise:
print(members)
