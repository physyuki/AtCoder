a, b = map(int, input().split())

ans = max(a, b)
ans += max(ans-1, min(a, b))
print(ans)