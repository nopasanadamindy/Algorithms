test = '1+2'
print(test)                 # 1+2
print(str(test))            # 1+2
print(repr(test))           # '1+2'
print(eval(str(test)))      # 3
print(eval(repr(test)))     # 1+2
print(eval(eval(repr(test)))) # 3
