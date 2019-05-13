x, a, b = map(int, [input() for i in range(3)])

ans = x - a
ans = ans % b
print(ans)