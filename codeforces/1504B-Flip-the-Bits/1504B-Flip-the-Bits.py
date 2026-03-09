t = int(input())

for _ in range(t):

    n = int(input())
    a = list(input())
    b = list(input())
    bal = [0] * n
    z = 0
    o = 0
    for i in range(n):
        if a[i] == '0':
            z += 1
        else:
            o += 1
        if z == o:
            bal[i] = 1
    flip = 0
    ok = True
    for i in range(n - 1, -1, -1):
        cur = a[i]
        if flip:
            if cur == '0':
                cur = '1'
            else:
                cur = '0'
        if cur == b[i]:
            continue
        if bal[i] == 0:
            ok = False
            break
        flip ^= 1
    if ok:
        print("YES")
    else:
        print("NO")