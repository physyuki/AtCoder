n, k = map(int, input().split())
s = list(input())
for i in range(n):
    if i == k-1:
        s[i] = s[i].lower()
        print(''.join(s))
        exit()
