def sum(T):
    c = [0] * 51
    for i in T:
        c[i] += 1
    m = 0
    for i in range(51):
        if c[i] > 0:
            c[i] -= 1
            m += 1
        else:
            break
    s = sum(i * c[i] for i in range(51))
    return m + s

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().strip().split()))
    print(sum(s))