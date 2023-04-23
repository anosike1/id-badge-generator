# print out this sentence
print ('Please enter the following information:')

# prompt the user to input values and bind them to variables
# the first name will be in Title case
# the last name will be in UPPER case
# the email address will be in lower case
f_name = input ("First name: ").title()
l_name = input ("Last name: ").upper()
email_add = input ("Email address: ").lower()
phone_num = input ("Phone number: ")
job = input ("Job title: ")
id_num = input ("ID Number: ")

# generate ID using the user inout variables
print (f"""
The ID Card is:
----------------------------------------
{l_name}, {f_name}
{job}
ID: {id_num}

{email_add}
{phone_num}
----------------------------------------

""")