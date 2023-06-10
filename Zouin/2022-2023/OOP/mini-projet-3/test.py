# ask for input and see how much time it took to answer
# make a separate function for each

import time

def ask_name():
    name = input("What is your name? ")
    print("Hello " + name + "!")

def ask_age():
    age = input("How old are you? ")
    print("You are " + age + " years old.")

def ask_birthday():
    birthday = input("When is your birthday? ")
    print("Your birthday is on " + birthday + ".")


start_time = time.time()
ask_name()
ask_age()
ask_birthday()
end_time = time.time()
print("It took you " + str(end_time - start_time) + " seconds to answer all the questions.")