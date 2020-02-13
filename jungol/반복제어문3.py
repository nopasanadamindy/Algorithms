# 550.
# num = int(input())
# i = 0 # 공백
# j = num # *
# while :
#     print('*' * j)
#     j -= 1
# while i < num:
#     print('*' * i)
#     i

#
# num = int(input())
# for i in range(num, 0, -1):
#     print('*' * i)
# for i in range(1, num + 1):
#     print('*' * i)
#
#
# for i in range(1, 2 * num + 1):
#     if i <= num: # 1, 2, 3
#         print('*' * i)
#     else: # 4, 5, 6
#         print('*' * (i - 3))
# #

# 551.
# num = int(input())
# i = 0 # 공백
# j = num # *
# while i < num:
#     print( (' ' * i) + ('*' * j))
#     i += 1
#     j -= 1

# 552.
# num = int(input())
# i = 0
# j = num
# while i < num:
#     print((' ' * i) + ('*' * j))
#     i += 2
#     j -= 2


# 144
# num = int(input())
# i = 0
# j = 0
# while i < num:
#     print((' ' * i))


# 149.

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end = ' ')
#     print()

# # 551.
# ***
#  **
#   *
# num = int(input())
# i = num # *
# j = num - i # ''
# while i >= 1:
#     print((i * ' ') + (j * '*'))
#     i -= 1

# [계단]
# num = int(input())
# i = 0
# while i < num:
# 	i += 1
# 	print('*' * i)

# [역경사]
# num = int(input())
# i = 0
# j = num - i
# while i < num:
#     i += 1
#     print(('' * (i - 1)) + ('*' * ((num + 1) - i)))


# [삼각형]
# num = int(input())
# i = 0
# while i < num:
#     i += 1
#     print((' ' * (6 - i)) + ('*' * (i * 2 - 1)))

# # [역경사]
# num = int(input())
# i = 0 #공백
# j = num - i # *
#
# while i < num:
#
#
# # 147.
# num = int(input())
# for i
#


# num = int(input())
# i = 1
# for _ in range(num):
#     for _ in range(num):
#         print(i % 10, end = ' ')
#         i += 2
#     print()


###ver1) range에서 i 자체를 홀수로
# for i in range(1, 9 + 1, 2):
#     pass
# for _ in range(num):
#     for _ in range(num):
#         print(i, end = ' ')
#     print()

# ###ver2) if문으로
# for i in range(1, 9 + 1):
#     if i % 2 == 1:
#         for _ in range(num):
#             for _ in range(num):
#                 print(i, end = ' ')
#             print()


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
print(fibo(8))