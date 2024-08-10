## WAP to split the string without using the split function.
# a = input('Enter the string:')
# res = []
# d = ''
# i = 0
# while i < len(a):
#     if a[i] == ' ':
#         res.append(d)
#         d = ('')
#     else:
#         d += a [i]
#     i += 1
# if d:
#     res.append(d)
# print(res)
#
## WAP to extract all the even numbers from the given homogeneous list.
# a = [10, 27, 35, 42, 59, 76]
# res = []
# i = 0
# while i < len(a):
#     if a[i] % 2 == 0:
#         res.append(a[i])
#     i += 1
# print(res)
#
## WAP to extract all the even numbers from the given heterogeneous list.
# a = [10, 22.7, 19, 'Annie', [10,20,30], True, False]
# res = []
# i = 0
# while i < len(a):
#     if type(a[i]) == int:
#         if a[i] % 2 == 0:
#             res.append(a[i])
#     i += 1
# print(res)
#
## WAP to extrct all the immutable items from the given heterogeneous list.
# a = [10, 22.7, 19, 'Annie', [ 10, 20, 30], 28, False, True, (11, 29, 39),{11,28, 42, 222}, {'a':'apple', 'b':'ball'}]
# res = []
# i = 0
# while i < len(a):
#     if not (isinstance(a[i],(list, set, dict ))):
#         res.append(a[i])
#     i += 1
# print(res)
#
## WAP to extract all the string items from the list if it has even length.
# a = [10, 22.7, 19, 'Annie', [ 10, 20, 30], 28, False, True, (11, 29, 39),'python','java']
# res = []
# i = 0
# while i < len(a):
#     if isinstance(a[i], str) and len(a[i]) % 2 == 0 :
#             res.append(a[i])
#     i += 1
# print(res)
#
## WAP to find the sum of first  n natural numbers.
# n = int(input('Enter the number:'))
# res = 0
# i = 1
# while i <= n:
#     res += i
#     i += 1
# print (res)
#
## WAP to find the factorial of a given number
# n = int(input('Enter the number:'))
# res = 1
# i = 1
# while i  <= n:
#     res *= i
#     i += 1
# print(res)

