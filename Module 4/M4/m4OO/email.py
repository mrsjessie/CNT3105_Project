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



import requests
import json

# Define Method to post data to API
def person_post(url, data):
    response = requests.post(url, data=json.dumps(data),
                                  headers={"Accept" : "application/json",
                                    "Content-Type":"application/json",
                                    "Authorization": "Bearer "+bearer})
    return response


#each user on a new line. 
filepath = "print(addresses)" 
# room to add new users
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vOTEyZDM2YzAtY2JiNS0xMWVhLWJmN2QtYjczZjdkZWRkNGM5" 
# add webex api admin token 
bearer = "YmQ0ZTIxNjktYThhMC00NDQ5LWEwZTgtNmVjM2JlNWFiZjU2OGI1OGZlNWQtNmIy_PF84_7fe15fed-c67b-4ddc-b29c-39338b4d309e" 


# empty list to hold the email addresses
emails = []
# open file to read the email addresses
with open(filepath, 'r') as read_emails:
    emails = read_emails.readlines()

# uncomment below line to check emails addresses are read from the text file
#print emails

# url to add new user to the room
add_membership_url = 'https://api.ciscospark.com/v1/memberships'

print
for email in emails: # every email address in the lines list
    try:
        param = {
        "roomId": room_id,
        "personEmail": email,
    }   

        # strip off any carriage return or new line characters from email
        person_email = email.strip('\r\n')

        # call the person_post method with 2 parameters, add_membership_url and payload
        result = person_post(add_membership_url,param)
        
        #print(result.status_code)

        if result.status_code == 409:
            print("{} - is already in the room.".format(person_email))
        elif result.status_code == 200:
            print("{} - is successfully added to the room.".format(person_email))
        else:
            result.json()
            print(result.status_code, result['message'])
        
        # uncomment below to see what error message is sent from the api
        #print(result.json())

    except Exception as e:
        print(e)
print
