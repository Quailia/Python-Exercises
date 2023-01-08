#Write a loop that prompts the user to enter a series of pizza toppings until they enter a quit value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True:
    t = input("What topping would you like on your pizza? (enter q to quit): ")
    if t == "q":
        break
    else:
        print(f"{t} has been added to your pizza.")