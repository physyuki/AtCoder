tar_len = input()
targets = map(int, input().split())

def how_many_times_divisible(elem):
    count = 0
    while True:
        if elem % 2 != 0: break
        count += 1
        elem = elem / 2
    return count

count = min(map(how_many_times_divisible, targets))
print(count)