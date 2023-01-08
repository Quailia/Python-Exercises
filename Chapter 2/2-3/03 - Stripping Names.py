#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#\t is a leading character, \n is a trailing character

name = ("\tFatima Ezzahraa\n")
print(name)
# rstrip removes both characters
a = name.strip()
print(a)
# rstrip removes only leading characters
b = name.lstrip()
print(b)
# rstrip removes only trailing characters
c = name.rstrip()
print(c)