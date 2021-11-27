l = [1,2,3,4,5,6,7,8,8]
duplicate = []
for i in l:
    if l.count(i) > 1 and i not in duplicate:
        print('Yes')
    else:
        print('No')