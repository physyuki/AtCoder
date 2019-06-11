n, k = map(int, input().split())
s = input()
a = s.lower()
print(s[:k-1] + a[k-1] + s[k:])
