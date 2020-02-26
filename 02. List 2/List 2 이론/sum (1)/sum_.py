T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # print(data)

    result = 0
    for y in range(100):
        sero = 0
        for x in range(100):
            sero += data[x][y]
        if sero > result:
            result = sero
    print(result)