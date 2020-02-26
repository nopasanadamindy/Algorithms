def my_strrev(ary):
    str = list(ary)
    for i in range(len(str)//2):
        # t = ary[i]
        # str[i] = str[len(str)-1-i]
        # str[len(ary) - 1 - i] = t
        str[i] , str[len(str) - 1 - i] =  str[len(str)-1-i], str[i]
    ary = "".join(str)
    return ary

ary = "algorithm"
ary = my_strrev(ary)
print(ary)

s = "Reverse this strings"
s = s[-1::-1]
print(s)
