n = int(input())
a = list(map(int, input().split()))
diff = []

for ai in a:
    for aj in a:
        diff.append(abs(ai - aj))
print(max(diff))
