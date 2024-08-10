# def add():
#     a = int(input('enter the number 1:'))
#     b = int(input('enter the number 2:'))
#     c = a + b
#     print(c)
#
#
# def Add(a, b, c):
#     d = a + b + c
#     return d
#
#
# x = Add(10, 20, 30)
# print(x)
#
#
# def div(a):
#     d = []
#     for i in range(1, a):
#         if a % i == 0:
#             d.append(i)
#     return d
#
#
# # # wap to check whether the entered number is prime number or not
# num = int(input('enter the number:'))
# if len(div(num)) == 1:
#     print('the entered number is primer number')
# else:
#     print('the entered number is not a prime number')
#
#
# # WAP to check whether the entered number is perfect or not
# num = int(input('enter the number:'))
# if sum(div(num)) == num:
#     print('the entered number is a perfect number')
# else:
#     print('the entered number is not a perfect number')
#
# a = int(input('enter the number 1:'))
# b = int(input('enter the number 2:'))
# if sum(div(a)) == b and sum(div(b)) == a:
#     print('the entered number are amicable numbers')
# else:
#     print('the entered numbers are not an amicable numbers')
#
# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f
#
#
# n = int(input('enter  the number'))
# res = 0
# i = n
# while i > 0:
#     res += fact(i % 10)
#     i //= 10
# if res == n:
#     print('strong')
# else:
#     print('week')

# Functions
# Creating a function without any parameters
# def greet():
#     print('Hello World')


# creating a function with a parameter
def greet_someone(name):  # name is a parameter / Argument
    # Function is not returning anything
    print(f"Hello {name}")


# creating  a function which returns a greeting to a mentioned name
def greet_someone(name):
    return f"Hello {name}"


# here name, age, pay are mandatory arguments
def msg(name, age, pay):
    return f"Hello {name} you are {age} years of age and you hget ${pay} as a pay"


def msg(name, age=18, pay=1000):  # name is mandatory argument, pay & age are optional
    return f"Hello {name} you are {age} years of age and you hget ${pay} as a pay"


def func(name, debug=False):
    if debug:
        print('You called Func function')
    return f"hello {name}"


# The arguments which are LHS of "/" will be considered as positional only arguments
def msg(name, /, age, pay):  # name is positional only argument
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


# The arguments which are RHS of "*" will be considered as key-word only arguments
def msg(name, *, age, pay):   # age, pay are keyword only arguments
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


def msg(name, /, *, age, pay):
    # name is positional only argument & age, pay are keyword only arguments
    return f"Hello {name} you are {age} years of age and you get ${pay} as a pay"


# in function call or in function definition key-word arguments should follow positional arguments.
# Positional arguments should never follow the keyword arguments
def msg(name, age, pay):
    return f"Hello {name} you are {age} years of age and you hget ${pay} as a pay"


def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c


# function which accepts any number of arguments and stores into args variable in the form of tuple
def func(*args):
    return args


# function which accepts minimum of 2 arguments to any number of arguments and returns sum of them
def add(a, b, *values):
    print(a)
    print(b)
    return values


def add(a, b, *args):
    res = a + b
    for i in args:
        res += i
    return res


# Function which accepts variable number of keyword arguments
def func(**kwargs):
    return kwargs