data = [list(0 for _ in range(5)) for _ in range (3)]
print(data)

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         print(j)

for y in range(len(data[0])):
    for x in range(len(data)):
        print(x)