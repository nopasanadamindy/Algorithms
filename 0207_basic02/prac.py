
#
# result = []
#
# for a in range(1, 50):
#     for b in range(1, 50):
#         for c in range(1, 50):
#             if c ** 2 == a ** 2 + b ** 2:
#                 result.append((a, b, c))
#

# result = [(a, b, c) for a in range(1, 50) for b in range(1, 50) for c in range(1, 50) if c ** 2 == a ** 2 + b ** 2]
# print(result)


# words = 'Life is too short, you need python!'

# result = []

# vowels = 'aeiou'
#
# result = [i for i in words if i not in vowels]
# print(''.join(result))
# for i in words:
#     if i not in vowels:
#         result.append(i)
# print(''.join(result))
#

# for i in words:
#     if i not in vowels:
#         result.append(i)
#
# print(''.join(result))

# my_dict = {'apple': '사과', 'banana': '바나나', 'grape': '포도'}
#
# my_dict['watermelon'] = '수박'
#
# print(my_dict)

# cubic = {x: x**3 for x in range(1, 8)}
# print(cubic)

dusts = {'서울':72, '대전':82, '구미':29, '광주':45, '중국':200 }

result = {}

print(result)