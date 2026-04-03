import random

name = input("What is your name? ")
print("hello " + name)

age = int(input("How old are you? "))
gpa = float(input("What is your GPA? "))

if gpa >= 3 and age >= 18:
    print("Congrats! You are accepted, you are a student now in CUS")
    is_student = True
    print("You are accepted")
else:
    print("You are rejected")

if age >= 18:
    print("You are an adult")
else:
    print("You are a child")

if age >= 18:
    print("Hello " + name + ", you are an adult so welcome to the game")

lucky_number = random.randint(1,6)

print("Your lucky number is " + str(lucky_number))
