# WAP to check the number is spy or not.
# a = int(input('Enter the number:'))
# s = 0
# p = 1
# i = a
# while i > 0:
#     s += i % 10
#     p *= i % 10
#     i //= 10
# if s == p:
#     print('The entered number is spy.')
# else:
#     print('The entered number is not spy.')


# def sp(a):
#     s = 0
#     p = 1
#     i = a
#     while i > 0:
#         s += i % 10
#         p *= i % 10
#         i //= 10
#     if s == p:
#         return True
#
# for x in range(1, 10000):
#     if sp(x):
#        print(x)

## WAP to check the entered number is amicable or not.
# a = int(input('Enter a number'))
# b = int(input('Enter a number'))
# i = 1
# c = 0
# d = 0
# while i<a:
#     if a %i == 0:
#         c += i
#     i += 1
# j = 1
# while j<b:
#     if b %j == 0:
#         d += j
#     j += 1
# if d== a and c == b:
#     print('The entered number is amicable.')
# else:
#     print('The entered number is not amicable.')

# for a in range(1000, 10000):
#     for b in range(a+1, 10000):
#         c = 0
#         d = 0
#         for i in range(1, a):
#             if a % i == 0:
#                 c += i
#         for j in range(1, b):
#             if b % j == 0:
#                 d += j
#         if a == d and b == c:
#             print((a, b))


# 0/P- (('Python', 'nohtyP', 6), ('is', 'si', 2), ('easy', 'ysae', 4))
# a = 'Python is easy'
# res = ()
# i = 0
# while i < len(a.split()):
#     w = a.split()[i]
#     res += (w, w[::-1], len(w)),
#     i += 1
# print(res)

# def func(a, res=(), i=0):
#     if i >= len(a.split()):
#         return res
#     else:
#         w = a.split()[i]
#         res += (w, w[::-1], len(w)),
#         return func(a, res=res, i=i +1)
#
# print(func('Python is easy'))
