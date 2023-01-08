#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

def make_shirt(size, message):
    print(f"\nThis t-shirt is {size}.")
    print(f"'{message}' is written on it.")
 
#Call the function once using positional arguments to make a shirt.
make_shirt("small", "Hello world.")

#Call the function a second time using keyword arguments.
make_shirt(size = "cat-sized", message = "Meow.")