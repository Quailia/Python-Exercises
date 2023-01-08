#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pets = []

Maxwell = {"name": "Maxwell", "species": "cat", "owner": "Kat", "trait": "chubby", "gender": "he"}
Pixie = {"name": "Pixie", "species": "cat", "owner": "Mat", "trait": "fluffy", "gender": "she"}
Finn = {"name": "Finn", "species": "cat", "owner": "Pat", "trait": "elegant", "gender": "he"}

pets.append(Maxwell)
pets.append(Pixie)
pets.append(Finn)

for cat in pets:
    print(f"About {cat['name']}: {cat['gender'].title()}'s a {cat['species']} that belongs to {cat['owner']}. {cat['gender'].title()}'s very {cat['trait']}.")
