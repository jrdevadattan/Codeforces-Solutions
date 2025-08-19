def out(T):
    ans, o, z = 0, 0, 0
    for i in range(len(T)):
        if T[i] == 0:
            z += 1
        elif T[i] == 1:
            o += 1
        ans += T[i]
    
    ans = ans + min(o, z)* 2 - min(o, z)
    if z > o:
        ans = ans + z - o
    return ans


num = int(input())
for _ in range(num):
    n = int(input())
    s = list(map(int, input().split()))
    print(out(s))
