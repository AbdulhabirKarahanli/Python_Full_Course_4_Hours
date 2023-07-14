secret_word = "Hoten"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you LOSE!")
else:
    print("You win!")

# Example
# Let me say, I want to make a guessing game that user make guess where I was born.
# Let me build the basic version of it first.

city_born = "Hoten"
guess = ""

while guess != city_born:
    guess = input("Where am I born? Guess it: ")

print("You won! Yes, I am from Hoten")


# Now, it is time to build more functional guessing game:

city_born = "Hoten"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != city_born and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input("Where am I born? Guess it: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You could not guess my city, You LOSE!")
else:
    print("You won! Yes, I am from Hoten, you are my man!!!")


# Well done!