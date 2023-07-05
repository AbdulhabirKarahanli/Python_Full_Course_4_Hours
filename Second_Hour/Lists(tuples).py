# Let us start with some basics about Lists in Python


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[0])
print(friends[2])
print(friends[-1])

# To call certain elements or a range in a list:
print(friends[1:]) # starting from index 1 and the rest
print(friends[1:3]) # starting from index 1 and taking 2 but 3 is not included.
print(friends[3:])

# I can change/modify the element of a list:
friends[1] = "Mike"
print(friends[1])

###########     List Functions       ###############

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

print(lucky_numbers)

# extend() function is used to append a list to the end of another list:
friends.extend(lucky_numbers)
print(friends)

# If we want to add another element to the end of our list, we can use append() function:
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
friends.append("Habir")
print(friends)

# What if we want to add an element to the middle of the list?
# In that case, we can use insert() function which takes two parameters:
# The first one is for index number where I want to insert the element
# The second one is the element itself.

print(friends)

# Let's say, I want to add "Ziya" for index 2.
friends.insert(2, "Ziya")
print(friends) # The rest of the elements are just pushed to the right side.

# To remove one element from the list: juts use remove() function:
friends.remove("Jim")
print(friends) # Jim is excluded now.

# To delete all elements of the list, just use clear() function
# friends.clear()
print(friends)

# To learn whether an element/name is inside of a list, we can do the following:
# For example, I want to check if Habir is present.
print(friends.index("Habir")) # It is there, index number 5.
print(friends[5])

# To know, how many same elements are in my list, we can use count()
friends = ['Kevin', 'Karen', 'Ziya', 'Oscar', 'Toby', 'Habir', 'Ziya']
print(friends.count("Ziya"))

# sort() is used to put these elements in alphabetical order
friends.sort()
print(friends)

# or can be used to put numbers in order:
lucky_numbers = [40, 18, 15, 16, 23, 42]
lucky_numbers.sort()
print(lucky_numbers)

# We can reverse the order of the elements in a list by .reverse() function:
# This is also works for strings in a list
lucky_numbers.reverse()
print(lucky_numbers)

# copy() function:
friends2 = friends.copy()
print(friends2)


########## Tuples ############

# It is very similar to lists in Python but just with a few key differences
# TUPLES ARE IMMUTABLE
# We can NOT change/modify the elements of a tuple as we did in lists.
# Tuples are stored with "()"; where lists are with [].
# However, if there are multiple tuples, then we can store them in a []. Still immutable.


coordinates = (4,5)
print(coordinates[0]) # we can access certain elements of a tuple by index numbers.

# Tuples are generally used for some values which you want to keep it safe and same.

coordinates = [(0,0), (1,3),(3,7), (4,9), (100,50)]
print(coordinates[0]) # pay attention to the difference.
print(coordinates[-1])


