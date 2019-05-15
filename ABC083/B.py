n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    d_sum = sum([int(tar) for tar in str(i)])
    if a <= d_sum <= b:
        ans += i

print(ans)