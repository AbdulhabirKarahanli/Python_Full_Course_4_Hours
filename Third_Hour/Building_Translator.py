# Aim: converting/translating every vowels into another consonants
# lets say we want to translate every vowels into "h"

def translate(phrase):
    translation = ""
    for lettler in phrase:
        if lettler in "AEIOUaeiou":
            translation = translation + "h"
        else:
            translation = translation + lettler
    return translation


print(translate(input("Enter a phrase: ")))


# Another way of keeping capital letter as it is:

def translate(phrase):
    translation = ""
    for lettler in phrase:
        if lettler.lower() in "aeiou":
            if lettler.isupper():
                translation = translation + "H"
            else:
                translation = translation + "h"
        else:
            translation = translation + lettler
    return translation


print(translate(input("Enter a phrase: ")))

