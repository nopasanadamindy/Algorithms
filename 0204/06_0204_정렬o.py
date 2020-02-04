
def sequence(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1

    if i < n and a[i] <= key:
        return i

    else:
        return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
data1= list(range(1,12))
key = 5


print(sequence(data, len(data), key))