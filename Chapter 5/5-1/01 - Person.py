#Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person = {"First Name": "Joanne", "Last Name": "Rowling", "Age": "Scotland", "City": "Edinburgh"}

#Printing dictionary as is
print(person)

#Printing dictionary in a readable format
for k, v in person.items():
    print(f"{k}: {v}")