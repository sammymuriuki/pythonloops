"""
STEP TWO

OK, now let's try printing out the information for each Danger Ranger member using a for loop -- this will be a
good start to printing a demand letter for each member.

Steps:

* Copy and paste the code from the previous step.
* Modify it here so instead of printing the entire `members` list in one line, you use a for loop to extract each
  member from the `members` list and print that member alone.
* Add comments before each block of code to explain what each block does.

"""
import json

members_file = open('member_info.json')    
members = json.load(members_file)
members_file.close()

""" iterate over the members list. each member is assigned to a variable called `member' """
for member in members:  
    """ print the contents of the member variable"""  
    print(member)
