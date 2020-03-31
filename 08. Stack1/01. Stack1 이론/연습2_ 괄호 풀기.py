'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
'''
# s = []
# def check_matching(data):
#     for i in range(len(data)):
#         if data[i] == '(':
#             s.append(data[i])
#         elif data[i] == ')':
#             if len(s) != 0:
#                 s.pop(-1)
#     if len(s) == 0:
#         return True
#     else:
#         return False

#
s = []
# 1) push
def push(item):
    s.append(item)

# 2) pop
def pop():
    if len(s) == 0:
        return
    else:
        s.pop(-1)

# 3) is_Empty
def is_Empty():
    if len(s) == 0:
        return True
    else:
        return False

# 4) check_matching
def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            push(data[i])
        elif data[i] == ')':
            if is_Empty() == False:
                pop()
    if is_Empty() == False:
        return False
    else:
        return True
data = input()
print(check_matching(data))