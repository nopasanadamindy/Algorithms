
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

