n, y = map(int, input().split())

for i in range(n + 1):
    for j in range(n +1 - i):
        k = n - i - j
        total = 10000 * i + 5000 * j + 1000 * k
        if total == y:
            print(i, j, k)
            exit()
print(-1, -1, -1)
