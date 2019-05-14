x, a, b = map(int, [input() for i in range(3)])

ans = x - a
while True:
    if ans - b < 0:
        break
    else:
        ans = ans - b

print(ans)