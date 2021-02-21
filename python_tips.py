"""
    String concatenation
"""
# names = ["Jeff", "Gary", "Jill", "Samantha"]
# for name in names:
# print("Hello " + name)
# print(' '.join(['Hello', name]))
# print(','.join(names))

# import os
# location = 'C:\\Users\\Lenovo\\.ssh'
# file = 'id_rsa.pub'
#
# with open(os.path.join(location, file, _)) as f:
#     print(os.sep)
#     print(f.read())

# who = 'Gary'
# how_many = 12
# # sentence = {}
# print(who,'bought', how_many, 'apples today!')
# print('{} bought {} apples today!'.format(who, how_many))# true way


"""
    Argument parser for command line
"""

# import argparse
# import sys
#
#
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0,
#                         help='What is the first number?')
#     parser.add_argument('--y', type=float, default=1.0,
#                         help='What is the second number?')
#     parser.add_argument('--operation', type=str, default="add",
#                         help='What operation? (add, sub, mul, or div)')
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))
#
#
# def calc(args):
#     operation = args.operation
#     x = args.x
#     y = args.y
#     if operation == 'add':
#         return x + y
#     elif operation == 'sub':
#         return x - y
#     elif operation == 'mul':
#         return x * y
#     elif operation == 'div':
#         return x / y
#
#
# if __name__ == '__main__':
#     main()
#
# # operation = calc(7, 3, 'div')
# # print(operation)

"""
    List and Generators
"""

# xyz = [i for i in range(5)]
# print(xyz)
# xyz = []
# for i in range(5):
#     xyz.append(i)
# print(xyz)

# xyz = [i for i in range(5000000000)]
# print(done)
# xyz = (i for i in range(5000000000)) #generator
# print(xyz)
# for i in xyz: #iterating over generator
#     print(i)


# input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
# xyz = (i for i in input_list if div_by_five(i))
# ## xyz = []
# ## for i in input_list:
# ##     if div_by_five(i):
# ##         xyz.append(i)
# [print(i) for i in xyz]

# [[print(i, ii) for ii in range(5)] for i in range(5)]
# # for i in range(5):
# #     for ii in range(5):
# #         print(i, ii)

"""
    Timeit - measure execution time of small code snippets
"""
# import timeit
#
# # print(timeit.timeit('1+3', number=50000000000))
#
# input_list = range(100)
# 
#
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
#
#
# xyz = (i for i in input_list if div_by_five(i))
# xyz = [i for i in input_list if div_by_five(i)]
#
# print(timeit.timeit('''input_list = range(100)
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# xyz = (i for i in input_list if div_by_five(i))
# for i in xyz:
#     x = i
# ''', number=5000))
# print(timeit.timeit('''input_list = range(100)
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False
# xyz = [i for i in input_list if div_by_five(i)]
# for i in xyz:
#     x = i''', number=5000))
"""
    Enumerate - the function that gives the count of the current iteration 
and the value of the item at the current iteration
"""
# example = ['left', 'right', 'up', 'down']
#
# for i in range(len(example)):  # <-- Wrong way
#     print(i, example[i])
#
# for i, j in enumerate(example):  # <-- Right way
#     print(i, j)
#
# new_dict = dict(enumerate(example))
# print(new_dict)
# [print(i, j) for i, j in enumerate(new_dict)]
"""
Zip
"""
# x = [1, 2, 3, 4]
# y = [7, 6, 2, 1]
# z = ['a', 'b', 'c', 'd']
#
# # for a, b, c in zip(x, y, z):
# #     print(a, b, z)
#
# print(dict(zip(x, y)))  # dictionary creation
#
# # [print(a, b) for a, b in zip(x, y)]
# # print(a)  # <-- 'a' is not defined
#
# for a, b in zip(x, y):
#     print(a, b)
# print(a)  # <-- last 'a' value is stored (4)
"""
More about generators 
"""
# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'
#
#
# for i in simple_gen():
#     print(i)
#
# CORRECT_COMBO = (3, 6, 1)
# found_combo = False
# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo: {}'.format((c1, c2, c3)))
#                 found_combo = True
#                 break
#             print(c1, c2, c3)


# def combo_gen():
#     for c1 in range(10):
#         for c2 in range(10):
#             for c3 in range(10):
#                 yield c1, c2, c3
#
#
# for(c1, c2, c3) in combo_gen():
#     print(c1, c2, c3)
#     if (c1, c2, c3) == CORRECT_COMBO:
#         print('Found the combo: {}'.format((c1, c2, c3)))
#         break
#     print(c1, c2, c3)
