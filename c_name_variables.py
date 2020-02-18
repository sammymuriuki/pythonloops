"""
STEP THREE

Now that we can print each member, let's try printing just each member's name and phone number.
We'll need to extract the details if we want to print demand letters.

Steps:

* Copy and paste the code from the previous step.
* Modify it here so instead of printing the entire list of facts about each member inside your for loop, you extract
    each fact into a separate variable that indicates its meaning, such as
    `name`, `phone_number`, `address`, `city`, `state`, `zip_code`, and `purchases`.
* Print just the name and phone number for each member.
* As usual, add comments before each block of code to explain what each block does.

(Why include this step? We *could* just refer to member[0] the entire time instead of using a new variable like "name".
But programming is easier if you move data around into variables that make sense to you.)

"""
import json

members_file = open('member_info.json')    
members = json.load(members_file)
members_file.close()

""" iterate over the members list. each member is assigned to a variable called `member' """
for member in members:  
    """ assign the first element of the member variable (index 0) to variable `name`"""  
    name = member[0]
    """ assign the second element of the member variable (index 1) to variable `phone_number`"""
    phone_number = member[1]
    """ assign the third element of the member variable (index 2) to variable `address`"""
    address = member[2]
    """ assign the fourth element of the member variable (index 3) to variable `city`"""
    city = member[3]
    """ assign the fifth element of the member variable (index 4) to variable `state`"""
    state = member[4]
    """ assign the sixth element of the member variable (index 5) to variable `zip_code`"""
    zip_code = member[5]
    """ assign the seventh element of the member variable (index 6) to variable `purchases`"""
    purchases = member[6]
    """ print the value of the variable `name`"""
    print(name)
    """ print the value of the variable `phone_number`"""
    print(phone_number)
