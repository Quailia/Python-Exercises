#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["pastrami sandwich", "pastrami sandwich", "pastrami sandwich", "chicken sandwich", "grilled cheese", "veggie sandwich", "tuna sandwich"]

finished_sandwiches = []

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
print("The deli has run out of pastrami.")

print("\n")
while sandwich_orders:
    s = sandwich_orders.pop()
    print(f"I made your {s}")
    finished_sandwiches.append(s)

print("\n")
for f in finished_sandwiches:
    print(f"A {f} was made.")