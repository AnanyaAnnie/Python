# # a= input('Enter the string:')
# # i=0
# # while i < len(a):
# #     if a[i].isupper():
# #         print(a[i])
# #     i +=1
#
# # WAP to extract all the char from one variable to another variable
# # a =input('enter the string:')
# # i = 0
# # res = ''
# # while i < len(a):
# #     res += a[i]
# #     i += 1
# #     print(res)
# #
# # WAP to Reverse the string (without using slicing)
# # a=input('Enter a string')
# # output=''
# # i = len(a)-1
# # while i>=0:
# #     output = output+a[i]
# #     i=i-1
# # print(output)
#
# # WAP to extract all uppercase alphabets from the given string
# # a = input('enter the string:')
# # i = 0
# # while i < len(a):
# #     if a[i].isupper():
# #          print(a[i])
# #     i += 1
#
# # WAP to replace the space charcter with underscore "_" from the given string
# a = input('Enter the string:')
# res = ''
# i = 0
# while i < len(a):
#     if a[i] == ' ':
#         res += '_'
#     else:
#         res += a[i]
#         i += 1
# print(res)
#
# # WAP to convert the given string into lowercase
# a=input('enter the string:')
# res=''
# i=0
# while i<len(a):
#     if 'A' <= a[i] <= 'Z':
#         res+=chr(ord(a[i])+32)
#     else:
#         res+=a[i]
#     i += 1
# print(res)

# # WAP to convert the given string into uppercase
# a=input('enter the string:')
# res=''
# i=0
# while i<len(a):
#     if 'a' <= a[i] <= 'z':
#         res += chr(ord(a[i])-32)
#     else:
#         res+=a[i]
#     i += 1
# print(res)
#
## WAP to Toggle the given string.
# a = input('enter the string:')
# res = ''
# i = 0
# while i < len(a):
#     if 'A' <= a[i] <= 'Z':
#         res = chr(ord(a[i]) + 32)
#     elif 'a' <= a[i] <= 'z':
#         res = chr(ord(a[i]) - 32)
#     else:
#         res += a[i]
#     i += 1
# print(res)
#
## WAP to remove the duplicate characters from the given string.
# a= input('Enter the string:')
# res = ''
# i = 0
# while i < len(a):
#     if a[i] not in res:
#         res += a[i]
#     i += 1
# print(res)
#
## WAP to separate the characters from the given string.
# a = input('Enter the string:')
# uc, lc, nc, sc = '','','',''
# i = 0
# while i < len(a):
#     if a[i].isupper():
#         uc += a[i]
#     elif a[i].islower():
#         lc += a[i]
#     elif a[i].isnumeric():
#         nc += a[i]
#     else:
#         sc += a[i]
#     i += 1
# print(i)
#
##WAP to find the number of uppercase alphabets in the given string.
# a = input('Enter the string:')
# c = 0
# i = 0
# while i < len(a):
#     if a[i].isupper():
#         c += 1
#     i += 1
# print(c)
#
## WAP to count the number of words in the given string.
# a = input('Enter the string')
# i = 0
# c = 0
# while i < len(a):
#     if a[i] == ' ':
#         c += 1
#     i += 1
# if a[-1] == ' ':
#     print(c)
# else:
#     print(c+1)
#

