def itoa(x):
    l_str = []
    y = 0
    while x:
        y = x % 10
        l_str.append(chr(y + ord('0')))
        x //= 10

    l_str.reverse()
    str = "".join(l_str)
    return str

x = 123;
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))

