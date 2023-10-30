
# LAMBDA FUNCTIONS
# Examples & Practice


# Write a lambda to...

# 1. given a number, triple it

def triple1(num):
    return num * 3

trip2 = lambda num: num * 3
print(trip2(1))


# 2. given a list of numbers, add 5 to each element
my_list = [1, 2, 3, 4, 5]
def add_five1(num) :
    return num + 5

add_five2 = lambda num: num + 5
result = list(map(add_five2, my_list))
print(result)


# 3. filter a list of numbers to numbers greater than 5
numbers = [1, 4, 5, 10, 200, 3000]
print(numbers)

def greater_than_five(number):
    if number > 5:
        return True
    else:
        return False

nums_greater_than_five = list(filter(greater_than_five, numbers))
print(nums_greater_than_five)


greater_than_five = lambda number: number > 5

# 4. reduce a list of numbers to their sum

from functools import reduce

numbers = [0, 5, 10, 20]
print(numbers)

def sum_of1(a, b):
    nums_sum = a + b
    return nums_sum

sum_of_nums = reduce(sum_of1, numbers)
print(sum_of_nums)

sum_of2 = lambda a, b: a + b
sum_of_nums = reduce(sum_of2, numbers)

# 5. filter a dictionary of students by a student name

students = [
    {'name': "Jane", 'age': 43, 'specialisation': 'Software'},
    {'name': "Priya", 'age': 24, 'specialisation': 'Data'},
    {'name': "Diana", 'age': 18, 'specialisation': 'Data'}
]


def find_priya1(student):
    if student['name'] == 'Priya':
        return True
    else:
        return False

# with Python function
result = list(filter(find_priya1, students))
print(result)

find_priya2 = lambda student: student['name'] == 'Priya'
# with named lambda
result = list(filter(find_priya2, students))
print(result)

# with anonymous function / using lambda directly
result = list(filter(lambda student: student['name'] == 'Priya', students))
print(result)

# IMPORTANT NOTES:

# These examples have shown just how easy lambda functions are.
# Still, there are a few uses where lambda functions should not be used!

#  - If you're doing anything more than a basic task, or want to call 
#    other methods, use a normal function. 

#  - Lambdas are great for one off, anonymous functions, 
#    but they must only have one single expression. 
 
#  - If your lambda starts growing in size and looking like a common expression, 
#    then it is probably time to refactor in to a stand alone normal function.
