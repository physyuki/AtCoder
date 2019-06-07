x = input()
fx = sum([int(i) for i in x])
if int(x) % fx == 0:
    print('Yes')
else:
    print('No')
