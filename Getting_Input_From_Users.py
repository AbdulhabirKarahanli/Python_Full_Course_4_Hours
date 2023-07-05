name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!" + "you are " + age + " years old.")


# Exercise !

# Basic Student Registration for Uyghur Student Union:

print("Student Registration for Uyghur Student Union")

print("Please enter the requested information below!")

name = input("student name:")
surname = input("stundent surname:")
age = int(input("age:"))
city = input("the city you were born:")
university = input("university you are studying in:")
major = input("your major:")


infos = [name, surname, age, city, university, major]

print("Saving your informations....")

print("student name:{}\nstudent surname:{}\nage:{}\nthe city s/he was born:{}"
      "\nthe university s/he is studying in:{}\nhis/her major:{}\n".format(infos[0], infos[1],
                                                                           infos[2],infos[3],
                                                                           infos[4],infos[5]))

print("Registration is successful, you are officially a member of Uyghur Student Union!")

