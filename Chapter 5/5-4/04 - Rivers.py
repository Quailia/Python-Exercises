#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {"Nile": "Egypt", "Ganges": "India", "Mississippi": "the United States"}

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for r, c in rivers.items():
    print(f"The {r} river is located in {c}.")

#Use a loop to print the name of each river included in the dictionary.
for r in rivers.keys():
    print(f"The {r} river is included in the dictionary.")

#Use a loop to print the name of each country included in the dictionary.
for c in rivers.values():
    print(f"{c.title()} is included in the dictionary.")