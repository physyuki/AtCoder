n = int(input())
a = list(map(int, input().split()))
al_val = 0
bo_val = 0

while a:
    al_val += max(a)
    a.remove(max(a))
    if not a: break
    bo_val += max(a)
    a.remove(max(a))

print(al_val - bo_val)
