"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

It is a loop script where address is the print, where if you put “y” yes then it will keep asking 
for another email address but if you put “n” no then it will break/stop the script.

"""


addresses = []

more = input("Do you have an email address to enter (y/n)? ")

while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
    
print(addresses)
