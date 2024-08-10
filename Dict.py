## WAP to find the number of times the specific character is repeated in the given string.
# a = 'Banana'
# res = {}
# i = 0
# while i < len(a):
#     res[a[i]] = a.count(a[i])
#     i += 1
# print(res)
#
##
# names = ['steve', 'allen', 'miller', 'sundri', 'chandan', 'purab', 'preetham', 'swagat']
# res = {}
# i = 0
# while i < len(names):
#     res[names[i]] = [names[i][:: -1],len(names[i])]
#     i += 1
# print(res)
#
##
# names = ['steve', 'allen', 'miller', 'sundri', 'chandan', 'purab', 'preetham', 'swagat']
# res = {}
# i = 0
# while i < len(names):
#     res[names[i]] = [names[i][:: 1],len(names[i])]
#     i += 1
# print(res)
#
# a = ['steve', 'allen', 'miller', 'sundri', 'chandan', 'purab', 'preetham', 'swagat']
# res = {}
# i = 0
# while i < len(a):
#     name = a[i]
#     if len(name) % 2 == 0:
#         res[name] = [name,len(name)]
#     else:
#         res[name] = [name[::-1], len(name)]
#     i += 1
# print(res)
#
## WAP to group the names WRT the first character.
# a = ['Steve', 'Allen', 'Sundri', 'Mark', 'Anna', 'Chandan', 'Clark', 'Mike']
# res = {}
# i = 0
# while i < len(a):
#     if a[i][0] in res:
#         res[a[i][0]].append(a[i])
#     else:
#         res[a[i][0]] = [a[i]]
#     i += 1
# print(res)
#
## WAP to group the words WRT the length
# a = ['Steve', 'Allen', 'Sundri', 'Mark', 'Anna', 'Chandan', 'Clark', 'Mike']
# res = {}
# i = 0
# while i < len(a):
#     if len(a[i]) in res:
#         res[len(a[i])].append(a[i])
#     else:
#         res[len(a[i])] = [a[i]]
#     i += 1
# print(res)
#
## WAP to
# a = ['Steve', 'Allen', 'Sundri', 'Mark', 'Anna', 'Chandan', 'Clark', 'Mike']
# res = {}
# i = 0
# while i < len(a):
#     j = a[i]
#     if len(j) % 2 != 0:
#         res[j] = (j[len(j)//2], len(j), j)
#     else:
#         res [j] = (j[:: -1], len(j))
#     i += 1
# print(res)

