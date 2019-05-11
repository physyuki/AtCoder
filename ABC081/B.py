tar_len = input()
targets = list(map(int, input().split()))

count = 0

while True:
    exist_odd = False
    for target in targets:
        if target%2 != 0:
            exist_odd = True
    if exist_odd: break
    count += 1
    targets = list(map(lambda x: x/2, targets))

print(count)