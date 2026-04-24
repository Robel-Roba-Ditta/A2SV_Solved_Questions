import sys
input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1
def dfs(a):
    if len(a) == 1:
        return 0
    mid = len(a) // 2
    l = dfs(a[:mid])
    r = dfs(a[mid:])
    if l == -1 or r == -1:
        return -1
    if a[0] < a[mid]: 
        if max(a[:mid]) < min(a[mid:]):
            return l + r
        else:
            return -1
    else:
        if max(a[mid:]) < min(a[:mid]):
            return l + r + 1
        else:
            return -1
for _ in range(t):
    m = int(data[index])
    index += 1
    p = [int(data[index + i]) for i in range(m)]
    index += m
    ans = dfs(p)
    print(ans)