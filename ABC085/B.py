n = int(input())
d = map(int, [input() for i in range(n)])

ans = len(set(d))
print(ans)