import functools

items = [1002,48,981,305,20]
x = functools.reduce(lambda a,b: a if (a > b) else b, items)

print(x)

# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)

# print(squared)

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))

# print(squared)

# # doubles the number you send in
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# # same function definition to make both functions
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))