#Turn your if-else chain from Exercise 4-2 into an if-elifelse chain.

#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.

def alien(x):
    if x == "green":
        print("You just earned 5 points.")
    elif x == "yellow":
        print("You just earned 10 points.")
    else:
        print("You just earned 15 points.")

alien_color = "green"

alien(alien_color)

alien_color = "yellow"

alien(alien_color)

alien_color = "red"

alien(alien_color)

