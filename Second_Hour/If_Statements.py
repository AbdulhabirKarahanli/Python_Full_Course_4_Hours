########### If Statement ############
# It is used to take decisions.

# Basic boolean variable

is_male = False
is_tall = False

if is_male or is_tall:  # at least, one of the conditions must be true.
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = False

if is_male and is_tall:  # both of the conditions must be true.
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

# Example

is_hungary = False
is_cloudy = True

if is_hungary:
    print("Make your breakfast!")
elif not (is_hungary) and is_cloudy:
    print("Just take your umbrella!")
elif not (is_hungary) and not (is_cloudy):
    print("Just take your shades")
else:
    print("You are ready to go!")


########### If Statement & Comparisons ############

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


# Example

def power_take(base, power):
    if power >= base != 1:
        return print("You hava a great number")
    else:
        return print("You have a small number")


print(power_take(2, 4))

