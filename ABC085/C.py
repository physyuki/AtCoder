n, y = map(int, input().split())

def find_a_candidate():
    for i in range(n + 1):
        for j in range(n +1):
            for k in range(n + 1):
                sum_bill = i + j + k 
                if sum_bill == n:
                    ans = 10000 * i + 5000 * j + 1000 * k
                    if ans == y:
                        print('{} {} {}'.format(i, j, k))
                        return
    print('{} {} {}'.format(-1, -1, -1))

find_a_candidate()
