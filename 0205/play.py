
l = [1, 2, 3, 4, 3, 2, 1]

result = []
for i in l:
    if i not in result:
        result.append(i)
print(l)
print(result)