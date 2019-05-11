tar_len = input()
targets = list(map(int, input().split()))

count = 0
end_flag = True

while end_flag:
    for target in targets:
        if target%2 != 0:
            print(count)
            end_flag = False
            break
    count += 1
    targets = list(map(lambda x: x/2, targets))