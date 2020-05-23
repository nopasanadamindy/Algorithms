#
# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
# def sol(phone_book):
#     for number in phone_book:
#         num = number
#         for phone in phone_book:
#             if num != phone:
#                 if num == phone[0:len(num)]:
#                     return False
#     else:
#         return True
# sol(phone_book)
# print(sol(phone_book))
#
# # phone_book = ["119", "97674223", "1195524421"]
#
# phone_book = ["123", "456", "789"]
# for i in range(len(phone_book)):
#     for j in range(len(phone_book)-1):
#         if len(phone_book[j]) > len(phone_book[j + 1]):
#             phone_book[j], phone_book[j+1] = phone_book[j+1], phone_book[j]
#
# def sol(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)-1):
#             if len(phone_book[j]) > len(phone_book[j+1]):
#                 phone_book[j], phone_book[j+1] = phone_book[j+1], phone_book[j]
#
#     for x in range(len(phone_book)):
#         for y in range(x+1, len(phone_book)-x):
#             if phone_book[x] == phone_book[y][0:len(phone_book[x])]:
#
#                 return False
#     else:
#         return True
#
# print((sol(phone_book)))

phone_book = ["123", "456", "789"]
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer