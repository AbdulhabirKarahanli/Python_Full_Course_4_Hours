########## Functions ############

print("Hello, Habir!")

# Creating a function to say hi to the user.

def say_hi (name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("John", "23")

# Example1

def favorites(color, movie, weather, city):
    print("My favorite color is " + color, " and movie is " + movie, "wheather is " + weather, " and "
            "lastly city is " + city)

favorites("blue", "Sarang", "Sunny","Hoten")

# Example 2

def power_taker(base, power):
    print(base ** power)
power_taker(2,3)


########## Return Statement ############

def cube(num):
    print("The cube of the number you entered is")
    return num*num*num

print(cube(3))
print(cube(4))

result = cube(5)
print(result)

# After Python sees the "return" keyword, when we define a new function, it stops and just execute the code.
# But, if we put a print command before it in will execute all of them. 














