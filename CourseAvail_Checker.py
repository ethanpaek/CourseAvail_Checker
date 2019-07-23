#Ethan Paek
#May 11th, 2019
#A Python script that will send a text to my cell phone if seats are available in a class on eCampus (Santa Clara University's website to check class availability) with Twilio API and Windows Task Manager

import requests
from twilio.rest import Client

#Twilio setup for my account ID and token
account_sid = "(enter Twilio account sid here)"
token = "(enter unique Twilio token here)"
client = Client(account_sid, token)

#Professor Dezfouli's CourseAvail site for Computer Networks that will be extracted
Base_url = 'https://www.scu.edu/apps/ws/courseavail/search/4100/ugrad/coen+146'

r = requests.get(Base_url)
json_file = r.json()

#print(json_file)

results = json_file['results']
checked = false

if(checked == false){
    for i in results:
        #Extract some useful info
        class_name = i['subject'] + i['catalog_nbr'] + ": " + i['class_descr']
        time = i['mtg_days_1'] + " " + i['mtg_time_beg_1']
        prof = i['instr_1']
        seats = int(i['seats_remaining'])
        number = i['class_nbr']

        #Info to show what class we are looking up
        print(class_name)
        print(time)
        print(prof)
        print("Seats: " + str(seats))
        print()

        #will print how many seats are left if the class is not full and checked is still false
        if(number == "91287" and seats > 0):
        message = client.messages.create(to="+19712263557", from_="+14259547920", body=("Your class " + class_name + " has " + str(seats) + " seats left!"))
        checked = true
}
