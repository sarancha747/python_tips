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
    Timeit
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