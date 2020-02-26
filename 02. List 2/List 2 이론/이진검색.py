# def binarySearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:        #검색성공
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#
#     return False # 검색실패


def binary(a, key):
    s = 0
    e = len(a)-1

    while s <= e:
        m = (s + e)//2
        if a[m] == key:
            return True
        elif a[m] < key:
            s = m + 1
        else:
            e = m - 1
    return False

def binary_j(a, s, e, key):
    if s >= e:
        return False
    else:
        m = (s + e)//2
        if a[m] == key:
            return True
        elif a[m] < key:
            binary_j(a, m+1, e, key)
        else:
            binary_j(a, s, m-1, key)
    return False
key = 7
# key = 22
data = [2,4,7,9,11,19,23]
print(binary_j(data, data[0], data[len(data)-1], key))