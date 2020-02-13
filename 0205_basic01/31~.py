
## 32
inp = 9
def binary(n):
    result = 0
    idx = 0
    while (n >= 1):
        remainder = n % 2
        n = n // 2
        result += (10 ** idx) * remainder
        idx += 1
    return result

# inp = int(input())
print(binary(inp))

## 34

## 1) 리스트를 잘라서?(짝/홀)

## 2) 함수 사용

# word = str(input())
# def reverse(word):
#     return word[::-1]
#
# def isPalindrome(word):
#     if reverse(word) == word:
#         return word + '\n' + '입력하신 단어는 회문(Palindrome)입니다.'
#     else:
#         return '아닙니다'
#
# print(isPalindrome(word))


## 35

##1)
# def RSP(p1, p2, x1, x2):
#     if x1 == x2:
#         print('비겼습니다!')
#
#     # p1이 이길때
#     if x1 == '가위' and x2 == '보':
#         print('가위가 이겼습니다!')
#     elif x1 == '바위'and x2 == '가위':
#         print('바위가 이겼습니다!')
#     elif x1 == '보' and x2 == '바위':
#         print('보가 이겼습니다!')
#
#     # p2가 이길때
#     if x2 == '가위' and x1 == '보':
#         print('가위가 이겼습니다!')
#     elif x2 == '바위'and x1 == '가위':
#         print('바위가 이겼습니다!')
#     elif x2 == '보' and x1 == '바위':
#         print('보가 이겼습니다!')
#
# p1 = input()
# p2 = input()
# x1 = input()
# x2 = input()
# RSP(p1, p2, x1, x2)

##2) list로 받기
# def RSP(p1, p2):
#
#

## 36

# inp = int(input())
# def divisor(number):
#     cnt = 0
#     for i in range(1, number + 1):
#         if number % i == 0:
#             cnt += 1
#     return cnt
#
# # print(divisor(12))
#
# def isdemical(number):
#     if divisor(number) == 2:
#         return '소수입니다.'
#     else:
#         return '아닙니다.'
#
# print(isdemical(inp))


## 37
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib (n-2)

num = int(input())
print(fib(num))

## 38
# a = [1, 2, 3, 4, 3, 2, 1]
# #1) set
# l = [1, 2, 3, 4, 3, 2, 1]
# ll = list(set(l))
# print(ll)
#
# # 2-1) for
# ll = []
# for i in l:
#     if i not in ll:
#         ll.append(i)
# print(ll)
#
# # 2-2) idx
# aa = []
# for i in range(len(a)):
#     if a[i] not in aa:
#         aa.append(a[i])
# print(aa)

# # 3) def
# def mkset(a):
#     return list(set(a))
#
# print(a)
# print(mkset(a))

## 39
# def isNum(a, b):
#     if b in a:
#         return '{} => True'.format(b)
#     else:
#         return '{} => False'.format(b)
#
# list = list(range(2, 10+1, 2))
# a = 5
# b = 10
# print(list)
# print(isNum(list, a))
# print(isNum(list, b))

## 40
# def factorial(num):
#     result = 1
#     while num != 1:
#         result *= num
#         num -= 1
#     return result
# print(factorial(5))

