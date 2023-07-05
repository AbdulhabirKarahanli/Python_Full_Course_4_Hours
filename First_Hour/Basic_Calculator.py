num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# result = num1 + num2

# print(result) # this is because Python interprets it as string.


# attention: If you give a decimal number this line of code won't work. Solution: float() function.
# result = int(num1) + int(num2)
# print(result)


result = float(num1) + float(num2)
print(result)


# Exercise: Hypotenuse Calculator

# Formula: a^2 + b^2 = c^2

a = int(input("give the length of a side:"))
b = int(input("give the length of b side:"))

c = (a**2 + b**2)**(0.5)

print("The length of c is:", c)
