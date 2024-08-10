# lambda, map, filter
# lambda: lambda is a keyword, which is used to generate an anonymous function
#   WAP to create a function to find the sum of two numbers
# add = lambda  b, : a + b

# WAP to convert the given lowercase character to uppercase
# # up = lambda a : chr(ord(a)-32)
#
# # WAP to check whether the given number is even or not
# even = lambda a : a % 2 == 0

#=WAP to find the list of square of all the numbers from 1 to 20
# def sq(a, b):
#     res = []
#     for i in range(a, b):
#         res.append(i*i)
#     return res

# sq = list(map(lambda a: a*a, range(1, 21)))
# print(sq)

# WAP to extract all the even numbers from 1 to 100
# evens = list(filter(lambda a: a % 2 == 0, range(1,100)))
# print(evens)

# WAP to find the square of all then even numbers from 1 to 100
# evens_squares = map(lambda a: a**2, filter(lambda a: a % 2 == 0,range(1, 101)))


# WAP to check whether the the entered number is prime or not.
# def div(n):
#     res = []
#     for i in range(1, n):
#         if n % i == 0:
#             res.append(i)
#     return res
#
# def is_prime(a):
#     return len(div(a)) == 1
#
#
# n = 11
# d = filter(lambda i: n%1 ==0, range(1,n))
# print((list(d)))
#
# n = 28
# d = filter(lambda i: n%1 ==0, range(1,n))
# p = lambda n: len(list(d)) == 1
# print(p(11))
#
# is_prime = lambda n:len(list(filter(lambda i: n %i == 0, range(1,n)))) == 1
# print(is_prime(28))

a = 'python'
a.sort()