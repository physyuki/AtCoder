n = int(input())
info = [list(map(int, input().split())) for i in range(n)]

info.insert(0, [0, 0, 0])
x_diff, y_diff = 0, 0

for i in range(n):
    dt = info[i+1][0] - info[i][0]
    x_diff = abs(info[i+1][1] - info[i][1])
    y_diff = abs(info[i+1][2] - info[i][2])
    if dt < x_diff + y_diff:
        print('No')
        exit()
    if dt%2 != (x_diff + y_diff)%2:
        print('No')
        exit()

print('Yes')
