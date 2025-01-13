# def check_3_digits(number):
#     return number in range (100,1000)

# result = check_3_digits(68)
# print(result)



# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass

# result = check_3_digits([55,99,6000])
# print(type(result))





# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             return False




# result = check_3_digits([555,999,600])
# print(result)





# parameter is list1
# def check_3_digits(list1):

#     three_digit_list = []                #empty list


#     for n in list1:
#         if n in range(100,1000):
#             three_digit_list.append(n)         
#             return True
#         else:
#             pass
     
#     return False


# result = check_3_digits([555,99,600])
# print(result)


# coffee_prices = [('cappuccino',1.5),
#                  ('exoressi',1.2),
#                  ('mocha',1.9)]


# def most_expensive_coffee(list_of_prices):
    
#     highest_price = 0
#     my_most_expensive_coffee = ' '

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass

#     return(my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))



# def most_expensive_coffee(list_of_prices):
    
#     highest_price = 0
#     my_most_expensive_coffee = ' '

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass

#     return(my_most_expensive_coffee, highest_price)

# coffee, price = most_expensive_coffee(list_of_prices)


# print(f'The most expensive coffee is {coffee}, whose price is {price}')





#Abel Sanchez, Diego Padilla, Lorenzo Gasca
# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def functions(all_positive):    # This sets the perimeter for the function
    for n in all_positive:      # This makes and iteration for n
        if n > 0:               # This checks if n is positive or negative
            return True         # If the argument is true then true will be the printed result
        else:
            return False        # If the argument is false then false will be the printed result


# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000,
# and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

numbers = [150, 20, 500]       # this makes the list of the numbers
def sum_less(numbers):                                      # This sets the perimeter for the function
    return sum(num for num in numbers if 0 < num < 1000)    # This ensures that the summed numbers are more than 0 and less than 1000


result = sum_less(numbers)                #this adds all the numbers and puts it into one variable
print(result)  #This prints the sum of the list 


# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), 
# and returns the result of said count.

list1 = [2, 4, 6, 7, 8]           #this makes a list for the numbers
def count_even(list1):          # This makes a perimeter for the function
    return sum(1 for num in list1 if num % 2 == 0)      #this ensures that the numbers are even

result = count_even(list1)   #this counts the even numbers and puts it into a new variable
print(result)               #this prints the amount of even numbers in the list



