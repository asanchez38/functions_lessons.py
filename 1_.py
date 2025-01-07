# functions are ways to wrap your code
# into reuseable units 
# I only define the function ONCE
# whatever i pass inside the parentheses 
# is called a paramter
# a parameter is a placeholder for future information
# def sayHello(name, age, address):
#     print(f"say Hello{name}")
#     print(f"Hello Govenor your address is {address}")
#     print(f"welcome back{name}")
#     print(f"your age is {age}")

# once you define a function
# you must call or invoke the function
# When I pass in information into the
# the called function, its called an argument
# sayHello(" evins", 34, "345 north landale")
# sayHello(" Devin", 24, "345 south landale")
# sayHello(" Lara", 45, "345 west landale")

# def determineEligiblity(age):   #age is the parameter
#     # If your age is over 18, you can vote,
#     # otherwise you cant
#     if age >=18:
#         print('you can vote')
#     else:
#         print('you have to wait')

# determineEligiblity(12)
# determineEligiblity(18)
# determineEligiblity(19)

# def WillYouGraduate(gpa,credit,SAT): # gpa, credit, and sat means it has 3 parameters
#     # gpa : number float varaible 
#     # credits :number varaible
#     # passed SAT : BOOLEAN
#     if(gpa == 3.0) and (credit == 20) and (SAT == True):
#         print("you passed. Good luck in College")
#     elif (gpa <3.0 ) or (credit < 20) or (SAT != True):
#         print('talk to your counselor')


# WillYouGraduate(2.0, 15, True)
# WillYouGraduate(3.0, 20, True)
# WillYouGraduate(1.0, 2, False)



# return = statement used to end a function
#          and send back to the caller

# z = 3

# def add(x,y):
#     z = x+y
#     return z 


# def subtract(x,y):
#     z = x-y
#     return z 

# def multiply (x,y):
#     z = x * y
#     return z 


# def divide (x,y):
#     z = x/y
#     return z 


# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(First, Last):
    First = First.capitalize()
    Last = Last.capitalize()
    return First + " " + Last

full_name = create_name("Spongebob", "squarepants")
print(full_name)

