#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

guests = ["Khajiit", "Arbogast", "Xavier"]

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

guests[0] = "Silverclaw"

#Print a second set of invitation messages, one for each person who is still in your list.

for x in guests:
    print(f"\nGood day, {x}. You are cordially invited to attend our dinner party at 7. Appropriate attire is required.\n")

#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

print(f"Unfortunately, Khajiit couldn't make it on time. {guests[0]} has decided to join us instead.")