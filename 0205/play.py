

def numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i + 1
    return numbers

print(numbers(5))

def countdown(num):
    while num > 0:
        return num
        num -= 1
    return '카운트다운을 하려면 0보다 큰 입력이 필요합니다.'
print(countdown(0))