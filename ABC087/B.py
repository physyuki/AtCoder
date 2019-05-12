a, b, c, x = map(int, [input() for i in range(4)])
count = 0

for a_num in range(a+1):
    for b_num in range(b+1):
        for c_num in range(c+1):
            if a_num * 500 + b_num * 100 + c_num * 50 == x:
                count += 1
print(count)