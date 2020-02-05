
i = 200

while 100 <= i <= 300:
    while i != 0 :
        if (i % 10) % 2 == 0:
            i = (i // 10)
            if (i % 2) == 0:
                print(i, end = ',')
        else:
            break