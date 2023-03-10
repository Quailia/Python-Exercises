#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

gls = {"String": "A sequence of characters.", "Variable": "Containers for storing data values.", "Function": "A statement which returns some value to a caller", "Dictionary": "An associative array, where arbitrary keys are mapped to values.", "Tuple": "A collection of objects which are ordered and immutable."}
 
for k, v in gls.items():
    print(f"{k}: {v}")