print(9)

print(9**2)
print(9**2 / 3)
print(7 * 7)

# % is very essential to know the remainder when making a division.

print(10 % 3) # the remainder is 1.

# Strong a value in a container/variable

my_num = 5
print(my_num)

# str() function is handy to convert a number into a string.

print(str(my_num) + " my favorite number.")

my_num = str(my_num)

print(5 * my_num) # since it is a string now, Python gives us the same string character 5 times.

my_num = int(my_num) # converted into a integer.
print(5 * my_num) # math calculations are possible now.


num_1 = -10

print(num_1)

print(abs(num_1)) # this abs() function gives us the absolute value of a number.

# Another function to take the power of a number:
print(pow(3,4))
print(3**4)

# To know, which number is higher and lower we can use max() and min() functions
print(max(2,3,4,5,7,8,9))
print(min(2,3,4,5,7,8,9))

# To round a decimal number to an integer, we can use round() function:
print(round(3.9))
print(round(3.2))

from math import *

print(floor(6.9)) # this will take directly the initial
print(ceil(6.1)) # this will take the next integer.
print(sqrt(100)) # square root of a number

print(log(100, 10)) #second is base.
print(sin(0))
print(cos(0))



