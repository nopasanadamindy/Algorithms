
# 오름차순 정렬
def selectionSort(a):
    for i in range(0, len(a) - 1):
        min = if j in range(i + 1, len(a)):
        if a [min] > a[j]:
            min = j
        a[i], a[min] = a[min], a[i]


data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)


# k번째값 정렬
def selection(a, k):
    for i in range(0, k):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

    return a[k-1]

def selectionSort(a):




    data = [64, 25, 10, 22, 11]
    selectionSort(data)
    print(data)
    print(selection(data, 3))