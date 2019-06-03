n = int(input())
t, a = map(int, input().split())
hs = map(int, input().split())
diff = []

for h in hs:
    diff.append(abs(a - (t - h * 0.006)))
print(diff.index(min(diff)) + 1)
