def out(arr, k):
    time = 0
    c = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            c += 1
        else:
            c = 0
        if c == k:
            time += 1
            c = 0
            i += 1
        i += 1
    return time

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    print(out(arr, k))