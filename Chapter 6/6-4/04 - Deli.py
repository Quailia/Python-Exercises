# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["chicken sandwich", "grilled cheese", "veggie sandwich", "tuna sandwich"]

finished_sandwiches = []

while sandwich_orders:
    s = sandwich_orders.pop()
    print(f"I made your {s}")
    finished_sandwiches.append(s)

print("\n")
for f in finished_sandwiches:
    print(f"A {f} was made.")