#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

guests = ["Silverclaw", "Arbogast", "Xavier"]

print(guests)

#Add a new line that prints a message saying that you can invite only two people for dinner.

print("\nIt has been decided that only two people can be invited to the dinner party.")

#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

popped_guest = guests.pop(2)

print(f"\n{popped_guest}, we regret to tell you that your invitation to our dinner party has been revoked.")

#Print a message to each of the two people still on your list, letting them know they’re still invited.

for x in guests:
    print(f"\nGood day, {x}. You are still invited to the dinner party. We hope to see you there.")

#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

del guests[:]
print(guests)