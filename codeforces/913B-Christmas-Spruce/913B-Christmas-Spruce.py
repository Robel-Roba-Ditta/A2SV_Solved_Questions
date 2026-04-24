n = int(input())
p = [0] * (n + 1)
ch = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    pi = int(input())
    p[i] = pi
    ch[pi].append(i)
leaf = [True] * (n + 1)
for i in range(1, n + 1):
    if ch[i]:
        leaf[i] = False
ok = True
for i in range(1, n + 1):
    if not leaf[i]: 
        cnt = 0
        for j in ch[i]:
            if leaf[j]:
                cnt += 1
        if cnt < 3:
            ok = False
            break
print("Yes" if ok else "No")