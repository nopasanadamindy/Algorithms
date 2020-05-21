import sys
sys.stdin = open('card.txt')

T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    cards = list(map(int, input()))
    dict = {}
    for i in range(len(cards)):
        if cards[i] not in dict:
            dict[cards[i]] = 1
        else:
            dict[cards[i]] += 1
    # print(dict)

    data = []
    for key, val in dict.items():
        data.append(key)
        data.append(val)
    # print(data)

    max_card = 0
    max_num = data[1]
    for i in range(0, len(data), 2):
        if data[i+1] >= max_num:
            if data[i+1] == max_num:
                if data[i] > max_card:
                    max_card = data[i]
            else:
                max_num = data[i+1]
                max_card = data[i]
    print('#{} {} {}'.format(test_case, max_card, max_num))


