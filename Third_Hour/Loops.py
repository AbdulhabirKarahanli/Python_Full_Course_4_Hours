############### While Loops #################

i: int = 1
while i <= 10:  # i <= 10, this part is the condition
    print(i)
    i += 1
print("Done with loop!")
# the scenario here is that, i=1 defined initially, our condition was i <= 10, so i=1 which
# satisfies the condition, that is why python prints it out and then add one (i += 1), then
# i becomes 1 + 1 = 2, then it goes back to our condition, same thing happens until i = 11.


# Example

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

############### For Loops #################

# It is used to loop over different collection of items, such as arrays, letters inside a string, or a series of
# numbers.

for letter in "Habir Academy":
    print(letter)

friends = ["Ziya", "Alishir", "Carullah"]
for friend in friends:
    print(friend)

for index in range(10): # 10 is NOT included
    print(index)

for index in range(3,10): # Starting from 3 and again 10 is NOT included.
    print(index)

for index in range(len(friends)):
    print(friends[index])

for i in range(5):
    if i == 0:
        print("First iteration")
    else:
        print("Not first iteration")


# Example

for i in range (0, 11):
    if i % 2 == 0:
        print("This is an even number")
    else:
        print('This is an odd number')


