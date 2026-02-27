t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    res = []
    res.append(p[0])  
    for i in range(1, n - 1):
        left = p[i - 1]
        cur = p[i]
        right = p[i + 1]

        if (left < cur > right) or (left > cur < right):
            res.append(cur)

    res.append(p[-1]) 

    print(len(res))
    print(*res)
