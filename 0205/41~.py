## 41

## 1-1)
# def square(a):
#     return 'square({}) => {}'.format(a, a**2)
# print(square(2))
# print(square(3))
#
## 1-2) input값만 다르게 받음/근데 왜 런타임에러나????
# a, b = map(int, input().split())
#
# def square(a):
#     return 'square({}) => {}'.format(a, a**2)
#
# print(square(a))
# print(square(b))

## 42

# a, b = map(str, input().split(', '))
# def long(a, b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b
#
# print(long(a, b))

## 43
def countdown(num):
    while num > 0:
        return num
        num -= 1
    return '카운트다운을 하려면 0보다 큰 입력이 필요합니다.'
print(countdown(0))
