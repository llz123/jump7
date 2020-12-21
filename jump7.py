#i = 0
#while i < 101:
#    i += 1
#    print(i)
#    for i in (7,17,27,37,47,57,67,77,87,97):
#        continue
#        i += 1
#    print(i)


#for i in range(101):
#    for i in (7,17,27):
#        continue
#       print(i)

"""
i = 0
while i < 100:
    i += 1
    if i % 7 == 0 or i // 10 ==7 or i % 10 ==7:
        continue
    else:
        print(i)
"""



for i in range(101):
    if i % 7 == 0 or i // 10 == 7 or i % 10 ==7:
        continue
    else:
        print(i)
