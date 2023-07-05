# Working with Strings in Python:

print("Habir\nAcademy") # \n is used for starting next line.

phrase = "Habir Academy"

print(phrase + " is cool!") # This part is called concatenation


# Very cool functions to work with strings

print(phrase.lower()) # this makes the entire line lower case.
print(phrase.upper()) # this makes the vice versa.

print(phrase.isupper()) # This function will give us true or false.

print(phrase.upper().isupper()) # True, because, firstly upper() is executed.

# To learn how many characters are in a string variable, we can use len() function.

print(len(phrase)) # There are 13 characters in "Habir Academy"

# If I want to get one of these characters in a string, I can use [] with a index number.

print(phrase[0]) # Do not forget that Python is zero-indexed.
print(phrase[-1]) # the last character.

print(phrase[5]) # this will give the space between Habir and Academy.

# Another awesome function to know the index number of a character in a string: index("parameter")

print(phrase.index("H")) # this will give me 0.
print(phrase[0]) # and this will give me H.

print(phrase.index(" "))
print(phrase[5])

# One more vital function to replace the values of strings: .replace("old", "new")

print(phrase)
print(phrase.replace("Habir", "Habo"))
print(phrase)

# If I want to make a permanent change in the variable and combine all I learned above, I can do the following

phrase = phrase.replace("Habir", "Habo")
print(phrase)

