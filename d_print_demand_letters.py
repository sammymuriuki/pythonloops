"""
STEP FOUR

Finally we have everything in place to print our demand letters -- we just need to assemble the facts about each
member into a string that contains the demand letter.

Steps:

* Copy and paste your code from the previous step.
* Modify it here so, after you extract the member information into variables, you build up a string consisting
  of a demand letter on behalf of that member, following the example in letters/sample_letter.txt.
* At the end of each loop, print the string containing the demand letter for that member.

Hints:

* You might want to start by copying and pasting the text from sample_letter.txt into this file, after the
  code you pasted in from the previous exercise.
* Printing 1000 letters can be annoying while you're trying things out. You can use a slice to cut the members list
  down to one or two while you experiment -- this is a handy trick in general.
* When you list the member's purchases, remember that your program should be able to deal with any
  number of purchases the member might have, not just the number of purchases that the first member happens to have.
* We haven't talked about how to print dollar figures with exactly two decimals, so don't worry if your dollar figures
  have too many decimals. As a stretch goal, if you have time, see if you can find the answer online.
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
    """ iterate through purchases of this member to get details of the items purchased. Assign each purchased item to a variable called `purchase` """
    letter = address + " " + city + ", " + state + " " + zip_code+ "February 9, 2018 "\
    """Herbie Humphrey 
    Herbie's House of Products 
    1 Goodvalue Place 
    Boston, MA, 01234
    Dear Mr. Humphrey: 
    I am writing to you under the provisions of Massachusetts General Laws, Chapter 93A, Section 9, the Consumer Protection Act.
    I am writing to request relief as outlined in that statute.
    On the following dates, the following unfair or deceptive acts or practices occurred: """
    total_amount = 0
    item = ""
    for purchase in purchases:
        purchase_date = purchase[0]
        item_name = purchase[1]
        price = float(purchase[2])
        behavior = purchase[3]
        total_amount = total_amount + price
        item += item_name
        letter += " * On " + purchase_date + " I purchased a " + item_name + " from your store, at a cost of " + str(price) + ". The product subsequently " + behavior + "."\
    "I believe that these acts or practices are declared unlawful by Section 2 of Chapter 93A, which declares unfair methods"\
    "of competition and unfair or deceptive acts or practices in the conduct of any trade or commerce unlawful."\
    "I have suffered injury or loss of money or property in the amount of " + str(total_amount) + "."\
    "This letter serves as my request for the following relief: refund of the above amount."\
    "Under the provisions of Section 9 Chapter 93A, I am providing you with the opportunity to make a written offer of"\
    "settlement of this claim within 30 days.  If you fail to make a good faith offer of settlement in response to this"\
    "request, and I institute legal action, a court may award me triple damages (amounting to a total of  " + str( total_amount*3 ) + " ),"\
    "as well as attorney’s fees and costs if the court finds in my favor."\
    "I may be reached at the address written above, or at " + phone_number + " between the hours of 9AM and 5PM.  I look forward to hearing from you."\
    "Sincerely, " + name
    print(letter)
