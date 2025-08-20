def out(T):
    val = None
    for i in T:
        if i == 0:
            return "NO"
        if i == -1:
            continue
        if val is None:
            val = i
        elif i != val:
            return "NO"
    return "YES"
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(out(a))