clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

count = {}
otjang = []
for cloth in clothes:
    otjang.append(cloth[0])
    if cloth[1] not in count:
        count[cloth[0]] = cloth[1]
    else:
        count[cloth[0]] += cloth[1]

final = []
for i in range(1 << len(otjang)):
    johap = []
    for j in range(len(otjang)):
        if i & (1<<j):
            johap.append(otjang[j])
    final.append(johap)

ans = 0
for johap2 in final:
    cnt = {}
    for item in johap2:
        if count[item] not in cnt:
            cnt[count[item]] = 1
        else:
            cnt[count[item]] += 1
    # print(cnt)
    for i in cnt:
        if cnt[i] != 1:
            break
    else:
        ans += 1
print(ans - 1)
