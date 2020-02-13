### 1. Reverse하기

s = "Reverse this strings"

def rev(ary):
    l = list(ary)
    result = []

    for i in range(len(l))[::-1]:
        result.append(i)
        return ''.join(result)

    ary = 'algorithm'
    print(rev(ary))

#
# def rev(ary):
#     str = list(ary)
#     for i in range(len(str)//2):
#         str[i], str[len(ary) - 1 - i] = str[len(ary) -1 - i], str[i]
#     return ''.join(str)
#
# ary = 'algorithm'
# print(rev(ary))
#
# s = 'Reverse this strings'
# print(s[::-1])
# ###리스트에 안넣어도 되뉴

### 2. <연습문제 2> str함수 쓰지 않고 itoa()구현/ 흐름을 파악하는 것이 중요

# def itoa(x):
#     result = []
#     str_result = ''
#     while x // 10 != 0:
#         r = x % 10
#         result.append(r)
#         x = x // 10
#     print(result)
    # for i in result:
    #     str_result += str(i)
    # return str_result
# x = 123
# print(itoa(x))


# 선생님 solution
# def itoa(x):
#     str = list()
#     y = 0
#
#     while True::
#         y = x % 10
#         str.append(chr(y + ord('0')))
#         x // = 10
# #         if x == 0 : break # while은
#
#     str.reverse()
#     str = "".join(str)
#     return str
# x = 123
# print(itoa(x))


### 3. <연습문제 3>

## 1) 고지식한 방법 : for문
# def bruteF(text, pat):
#     for i in range(len(text) - len(pat) + 1):
#         for j in range(len(pat)):
#             if text[i + j] != pat[j]:
#                 break
#         else:
#             return i
#
#
# def bruteF(t, p):
#     for i in range(len(t) - len(p) + 1):
#         cnt = 0
#         for j in range(len(p)):
#             if t[i + j] != p[j]:
#                 break
#             else:
#                 cnt += 1
#
#         if len(p) == cnt:
#             return i

# text = "TTTAACCA"
# pattern = "TTA"
# print("{}".format(bruteForce(text, pattern)))


# ## 2)  고지식한 방법 : while 문

### ver1)
# def bruteforce(text, pattern):
#     # i = 0 # text의 idx
#     # j = 0 # pattern의 idx
#     # while i < len(text) and j < len(pattern):
#     #     if text[i] != pattern[j]:
#     #         i = i - j
#     #         j = -1
#     #     else:
#     #         i = i + 1
#     #         j = j + 1
#     #
#     # if j == len(pattern):
#     #     return i
#     # else:
#     #     return -1

### ver2)
# def bruteforce(text, pattern):
#     i = 0  # text의 idx
#     j = 0  # pattern의 idx
#     while j < len(pattern) and i < len(text):
#         if text[i] != pattern[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#
#     if j == len(pattern):
#         return i
#     else: return -1

# text = 'This is book'
# pattern = 'is'
# print("{}".format(bruteFore(text, pattern))

# print(text.find(pattern))


### problem