t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    p = 0
    d = 0
    while a:
        cap = c // (2**d)
        pos = -1
        for i in range(len(a)):
            if a[i] <= cap:
                pos = i
        if pos != -1:
            a.pop(pos)
        else:
            a.pop()
            p += 1
        d += 1
    print(p)
