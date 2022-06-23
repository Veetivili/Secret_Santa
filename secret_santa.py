import os.path
import random
import uuid
from source import participant, secret_santa

# l is for prints, separating outputs.
l = "#############################################################################################"

myParticipants = {}
id_list = []

#Create while loop that continues asking user for participants, for every participant unique id is created aswell.
while True:
    id = str(uuid.uuid4())[:4]
    new_participant = participant(input("Participant name: "), id)
    myParticipants[id] = new_participant
    id_list.append(id)
    response = input("Do you want to add more participants? (yes/no): ")
    if not response:
        continue
    if response.lower() != 'yes':
        break

total_participants = len(myParticipants)

ask_budget = int(input("Insert your company budget: "))

#This fuction divides budget py participants.
def budget_per_gift():
    return round(ask_budget / total_participants, 2)

# As many gifts as participants are added to list. Gifts are taken from gifts.txt file and added to list.
gift_list = []
for i in range(total_participants):
    f = open('gifts.txt', 'r')
    for line in f:
        gift_list.append(line.strip())

gift_reciever = []
gift_lottery = []
rounds = 0

# While loop adds random participants to lists giver, gift and receiver. 
# It will recognize objects with them unique ID's. Before adding ID's
# to lists it will remove used ID's from gift_list.
while rounds < total_participants:
    gift_giver = id_list[rounds]
    random_id = random.choice(id_list)
    random_gift = random.choice(gift_list)
    if random_id == gift_giver or random_gift in gift_reciever:
        continue
    gift_list.remove(random_gift)
    gift_reciever.append(random_id)
    gift_lottery.append((gift_giver, random_gift, random_id))
    rounds += 1

x = []
i = 0
#this loop adds giver, gift and receiver to secret_santa class.
for i in gift_lottery:
    randomize = secret_santa(myParticipants[i[0]], i[1], myParticipants[i[2]])
    x.append(randomize)

print(l)
for secret_santa in x:
    print("Gift giver:",secret_santa.giver, "gift:", "|", secret_santa.present, "|" "gift receiver:",secret_santa.receiver)
print(l)
#In this point programm prints cost per gift and number of participants.
print("Participants for secret santa: ", str(total_participants), " | ", "Gift value for participant:", budget_per_gift(), "€")
print(l)



