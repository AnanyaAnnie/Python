## WAP to get the list of divisors of the given number.
# a = 6
# i = 1
# res = []
# while i < a:
#     if a % i == 0:
#         res.append(i)
#     i += 1
# print(res)
#
## WAP to check whether the entered number is prime number or not
# a =int(input('Enter the number:'))
# res = []
# i = 1
# while i < a:
#     if a % 1 == 0:
#         res.append(i)
#     i += 1
#
# if len(res) == 1:
#     print('The entered number is prime')
# else:
#     print('The entered number is not prime')
#
## WAP to check whether the number is perfect number or not.
# a =int(input('Enter the number'))
# res = 0
# i = 1
# while i < a:
#     if a % 1 == 0:
#         res += i
#     i += 1
#
# if res == a:
#     print('The number is perfect number')
# else:
#     print('The number is not perfect number')
#
## WAP to check whether the number is strong number or not.
# a = int(input('Enter the number:'))
# res = 1
# i = 1
# while i < a:
#     if a % i == 0:
#         res*= i
#     i += 1
#
# if res == 0:
#     print('The entered number is strong number')
# else:
#     print('The entered number is not strong number')
#
## WAP to check the number is Spy number or not.
# a =int(input('Enter the number:'))
# s = 0
# p = 1
# i = 1
# while i < a:
#     if a % i == 0:
#         s +=i
#         p *=i
#     i += 1
#
# if s == a and p == a:
#     print('The entered number is Spy number')
# else:
#     print('The entered number is not Spy number')
#
## WAP to check the number is Amicable number or not.
# a = int(input('Enter the number:'))
# c = 0
# i = 1
# while i < a:
#     if a % i == 0:
#         c += i
#     i += 1
#
# b = int(input('Enter the number:'))
# d = 0
# j = 1
# while j < b:
#     if b % j == 0:
#         d += j
#     j += 1
#
# if a == d and b == c:
#     print('The entered number is Amicable number')
# else:
#     print('The entered number is not Amicable number')
#
## WAP to find the sum of the divisors of the given numbers.
